# Twitter-sentiment-analysis

# NLP Models

The following code is meant to train NLP models on a corpus 
of tweets. Under are some instructions on how to use it in details
but let's first describe the most useful work-arounds.

Every python script that is meant to be run by the user uses
the library argparse, that allows you to feed the program the
argument it needs to work, when you don't know what arguments to
feed to a program, don't worry, and ask for help

```
python my_script.py -h
```

It will show you the list of argument needed, 
with some explanation.

For simplicity & educational purpose, some shell scripts calling
the python scripts with the right arguments are available,
you can run them with.

```
shell my_script.sh
```

However, you may run into trouble if you call these scripts 
without creating the dictionnary they use. The directories I
mention in this script are Data/ and Models/ . They are suppose to
contain respectively the tweets and several subsets of them, and
the machine learning models as well as the CountVectorizer 
objects. So before starting, you should call:

```
mkdir Models Data
```

## Training

Ok now let's dive into the subject. Before experimenting with a
model you need to train it. 

### Extraction of the training set

Files concerned:
    - brexit_tweets_all.jsonl ( you have to download it )
    - config.json
    - get_labeled_data.py

First, you need to build the training data by selecting 
which hashtags are "for brexit" and which are "against brexit"
this is done in the config.json file.

Now you can extract the number of tweets you want by calling
the script get_labeled_data.py. It takes as argument the input 
and output files, the configuration file and the number of tweets
to extract. Be aware that if they aren't enough tweets satisfying
the requirements in the initial file, it won't work.

```
python get_labeled_data.py --input brexit_tweets_all.jsonl --output Data/training.jsonl --limit 10000 --config config.json
```

This both filters tweets of the wanted hashtags and annotate every
tweet by adding a sentiment key, equal to 0 ( against brexit ) or
1 ( for brexit ).

### Creation of the tokenizer ( CountVectorizer )

Files concerned:
    - create_tokenizer.py
    - create_tokenizer.sh

In order to train a model on a corpus of text you need to be 
able to turn this corpus into a matrix containing one example
per line. This is what the CountVectorizer does. This object will
be trained on a corpus and will link an index to every word
(also lists of words optionnaly ) under certain condition.

Before creating this object, you can tune it's parameter by
modifying the source python file ( ye that's dirty ).

### Actual Training

Now that we have a training set and an object to turn 
sentences into vectors we can train any machine learning model
that we want. The one currently available are SVM, Naive Bayes, 
RandomForest and Multi Layer Perceptron.

To train a model, run one of this file like that

```
python model_file.py --input Data/training.jsonl --model 
Models/my_model.p --tokenizer Models/my_tokenizer.p
```

The script will print the final accuracy on the test set and
will save the model into the given file.


## Evaluation of performance

Files concerned:
    - evaluate.py

This file only contains one function that gives some more precise
metrics on a model. It is called at the end of training the
multi layer perceptron.

## Prediction and Interaction

Files concerned:
    - interact_with_model.py
    - label_new.py
    - label_new.sh    

Important thing to note: If you want your model to work
correctly, you have to use the same CountVectorizer object it
has been trained with, so to save a model, save both
the CountVectorizer object and the model.

Open the interact_with_model.py script in interpretation mode
to use the function predict("my text").

```
python interact_with_model.py --model Models/my_model.p --tokenizer Models/my_tokenizer.p
```

The file label_new.py can be used to label a new unseen collection
of tweets, you can then judge yourself if the tweets have been 
annotated correctly.
