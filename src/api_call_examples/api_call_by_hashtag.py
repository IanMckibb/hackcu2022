import json
from twitter_stream import FilteredStream

global stream

def delete_rules():
        curr_rules = stream.get_rules()
        print(curr_rules)
        rule_ids = []
        print("BEFORE: ", curr_rules)
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

# Rules to modify
rules: list = [
    {"value": "(ukrainian OR ukraine) lang:en"}
]

# Get rid of previous rules
delete_rules()

# Add current rules
stream.add_rule(data={"add": rules})

# While connected, print rules
for tweet in stream.connect():
    print(json.dumps(tweet, indent=4))