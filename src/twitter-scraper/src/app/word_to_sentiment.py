from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
from twitter_stream import FilteredStream
from scipy.special import softmax
import urllib.request
import numpy as np
import csv, json, sys

global stream
global tokenizer
counter = 100

def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)


def delete_rules():
        curr_rules = stream.get_rules()
        rule_ids = []
        if curr_rules['meta']['result_count'] != 0:
                rule_ids = {
                        "delete": {
                                "ids": [n['id'] for n in curr_rules['data']] # example id
                        }
                }
                stream.delete_rule(rule_ids)

def get_score(text):
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    # print(text)
    tempScore = 0.0
    for i in range(scores.shape[0]):
        l = labels[ranking[i]]
        s = scores[ranking[i]]
        mult = 0
        if l == 'negative':
            mult = -1
        elif l == 'positive':
                mult = 1
        tempScore += mult * s
    return tempScore

class Stream(FilteredStream):
    user_fields = ['name', 'location', 'public_metrics']
    expansion = ['author_id']
    tweet_fields = ['created_at']

# # Check to make sure user gave word
if len(sys.argv) <= 1:
    print("Please enter your phrase as a command line argument")
    exit()

word = " ".join(sys.argv[1:])

# Stream to read from
stream = FilteredStream()

# print("Enter input: ", end="")
# word = input()

# print("Current Word: ", word)

# Rules to modify
rules: list = [
    {"value": word + " lang:en -is:retweet"}
]

# Get rid of previous rules
delete_rules()

# Add current rules
stream.add_rule(data={"add": rules})

# While connected, print rules
inputStr = ""
for tweet in stream.connect():
    if counter <= 0:
            break
    counter -= 1
    cleaned = tweet['data']['text'].replace('\n', ' ').split()
    # cleaned = " ".join([n for n in cleaned if isValid(n)])
    cleaned = " ".join([n for n in cleaned])
    inputStr += (cleaned + '\n')

#######################

task='sentiment'
MODEL = f"cardiffnlp/twitter-roberta-base-{task}"

# tokenizer = AutoTokenizer.from_pretrained(r"~/Downloads/twitter-roberta-base-sentiment", from_tf=True)
tokenizer = AutoTokenizer.from_pretrained(MODEL)

# download label mapping
labels=[]
mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
with urllib.request.urlopen(mapping_link) as f:
    html = f.read().decode('utf-8').split("\n")
    csvreader = csv.reader(html, delimiter='\t')
labels = [row[1] for row in csvreader if len(row) > 1]

# PT
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
model.save_pretrained(MODEL)
tokenizer.save_pretrained(MODEL)

total_score = 0.0

# print("Getting scores...")

for text in inputStr.split('\n'):
    temp_score = get_score(text)
    total_score += temp_score
# print("Total Score: ", total_score)
print(total_score)
