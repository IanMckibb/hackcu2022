import json
from twitter_stream import FilteredStream

global stream
global counter
counter = 20

def isValid(n):
        for q in n:
                if (q >= 'a' and q <= 'z') or \
                        (q >= 'A' and q <= 'Z') or \
                        (q == '.' or q == '!' or q == '?'):
                        pass
                else:
                        return False
        return True

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

class Stream(FilteredStream):
    user_fields = ['name', 'location', 'public_metrics']
    expansion = ['author_id']
    tweet_fields = ['created_at']

# Stream to read from
stream = FilteredStream()

print("Enter input: ", end="")
word = input()

# Rules to modify
rules: list = [
    {"value": word + " lang:en -is:retweet"}
]

# Get rid of previous rules
delete_rules()

# Add current rules
stream.add_rule(data={"add": rules})

# While connected, print rules
with open('file.out', 'w', encoding='utf-8') as f:
        for tweet in stream.connect():
                if counter <= 0:
                        break
                counter -= 1
                cleaned = tweet['data']['text'].replace('\n', ' ').split()
                # cleaned = " ".join([n for n in cleaned if isValid(n)])
                cleaned = " ".join([n for n in cleaned])
                f.write(cleaned + '\n')
