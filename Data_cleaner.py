import jsonlines

simple_keys = ['created_at', 'full_text']
result = []

with jsonlines.open('brexit_tweets_all.jsonl') as reader:
    with jsonlines.open('output.jsonl', mode='w') as writer:
        for i in range(1000):
        #for tweet in reader:
            tweet = reader.read()
            if tweet['lang']=='en':
                my_dict={}
                for key in simple_keys:
                    my_dict[key]=tweet[key]
                my_dict['user_id'] = tweet['user']['id']
                my_dict['hashtags'] = tweet['entities']['hashtags']
                for hashtag in my_dict['hashtags']:
                    hashtag['text'] = hashtag['text'].lower()
                my_dict['symbols'] = tweet['entities']['symbols']
                writer.write(my_dict)