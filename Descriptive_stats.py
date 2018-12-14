import jsonlines
import matplotlib.pyplot as plt
import seaborn as sns

hashtag_dict = {}
language_dict = {}
users = set()

with jsonlines.open('output.jsonl') as reader:
    #for tweet in reader:
    for i in range(500):
        tweet = reader.read()
        
        users.add(tweet['user_id'])
        
        hashtags = tweet['hashtags']
        hashtag_list=[]       
        for hashtag in hashtags:
            hashtag_list.append(hashtag['text'])
        for hashtag in hashtag_list:
            try:
                hashtag_dict[hashtag] += 1
            except:
                hashtag_dict[hashtag] = 1
            
def dict_to_hist(d):
    lbl = []
    val = []
    for item in d.items():
        lbl.append(item[0])
        val.append(item[1])
    sns.set(style="darkgrid")
    ax = sns.barplot(x=lbl, y=val)
    fig = ax.get_figure()
    return fig

def dict_to_pie(d):
    lbl = []
    val = []
    for item in d.items():
        lbl.append(item[0])
        val.append(item[1])
    plt.pie(val, labels=lbl)

def dict_to_list(d, top = 50):
    lbl = []
    val = []
    for item in d.items():
        lbl.append(item[0])
        val.append(item[1])
    return [x for _,x in sorted(zip(val,lbl), reverse = True)][:top]


#fig = dict_to_hist(language_dict)
#fig.savefig('language_barplot.png')
#fig = dict_to_pie(hashtag_dict)
#fig.savefig('hashtag_barplot.png')
print(dict_to_list(hashtag_dict))