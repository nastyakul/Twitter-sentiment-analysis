#!/usr/bin/env python3
""" File containing some useful fonctions for preprocessing tweetsin order to feed them to a learning model """
import jsonlines
import numpy as np

keys = ["leaveeu", "voteleave","remain","voteremain"]

def preprocess_tweet(tweet):
    """ Function removing hashtags and citations from text 
    You only need to use it while training to prevent the 
    hashtags used for labelling to stay in the tweet """
    # Process the tweet
    indices = []
    for hashtag in tweet["hashtags"]:
        for key in keys:
            # Destroy the informative hashtag
            if hashtag["text"] == key:
                # Destroy the hashtag
                i1, i2  = hashtag["indices"]
                indices.append((i1, i2))
    indices.sort()
    if len(indices) == 0:
        reconstructed = tweet["full_text"]
    else:
        reconstructed = ""
        i1, i2 = indices.pop(0)
        stop = False
        for i, letter in enumerate(tweet["full_text"]):
            if i == i1:
                # Don't write
                stop = True
            if i == i2:
                stop = False
                if len(indices) > 0:
                    i1, i2 = indices.pop(0)
            if not stop:
                # Write
                reconstructed = reconstructed + letter
    return reconstructed

def train_on_docs(filename, t):
    # Create the document list and the Y list
    with jsonlines.open(filename) as reader:
        docs = []
        for tweet in reader:
            text = preprocess_tweet(tweet)
            docs.append(text)
    #t.fit_on_texts(docs)
    t.fit(docs)
    return t

def get_doc_list(filename, t):
    """ Encodes the tweets present into the given file
    in a one hot encoding fashion, returns the encoded docs
    and the labels """
    # Create the document list and the Y list
    with jsonlines.open(filename) as reader:
        docs = []
        labels = []
        for tweet in reader:
            text = preprocess_tweet(tweet)
            docs.append(text)
            labels.append(tweet["sentiment"])

    # Encode the documents
    encoded_docs = t.transform(docs)

    labels = np.array(labels)

    return encoded_docs, labels
