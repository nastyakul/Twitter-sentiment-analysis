#!/usr/bin/env python3
""" File containing some useful fonctions for preprocessing tweetsin order to feed them to a learning model """
import jsonlines
import numpy as np

def preprocess_tweet(tweet):
    """ Function removing hashtags and citations from text """
    tweet = tweet.split()
    reconstructed = ""
    for word in tweet:
        if "#" in word:
            # Replace all hashtags by the same null hashtag
            word = "#"
        if "@" in word:
            # Replace all citation by the same null citation
            word = "@"
        else:
            reconstructed = reconstructed + word + " "
    return reconstructed

def train_on_docs(filename, t):
    # Create the document list and the Y list
    with jsonlines.open(filename) as reader:
        docs = []
        for tweet in reader:
            text = preprocess_tweet(tweet["full_text"])
            docs.append(text)
    t.fit_on_texts(docs)
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
            text = preprocess_tweet(tweet["full_text"])
            docs.append(text)
            labels.append(tweet["sentiment"])

    # Encode the documents
    encoded_docs = t.texts_to_matrix(docs, mode="binary")

    labels = np.array(labels)

    return encoded_docs, labels
