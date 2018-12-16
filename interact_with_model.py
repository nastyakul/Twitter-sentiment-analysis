#!/usr/bin/env python3
""" Provides functions to interact with models, launch it in
interactive mode and provide it a model and a tokenizer 
WARNING: It is recommended that the model has been trained
with the same tokenizer to obtain correct results """
import pickle
import argparse
from preprocessing import preprocess_tweet

def predict(text):
    """ Feeds the text into the model and output it's prediction """
    # Preprocess the tweet text
    text = preprocess_tweet(text)
    # Turn it into an input vector
    vector = tokenizer.texts_to_matrix([text], \
    mode='binary')
    # Feed it into the model
    sentiment = model.predict(vector) 
    # Register the sentiment
    print("Stay:{0:10.4f}, Leave:{1:10.4f}".format(sentiment[0][0], sentiment[0][1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=argparse.FileType("rb"))
    parser.add_argument("--tokenizer", \
    type=argparse.FileType("rb"))
    args = parser.parse_args()
    tokenizer = pickle.load(args.tokenizer)
    model = pickle.load(args.model)
    print("\nUse predict(text) to explore what your model \
is thinking")
