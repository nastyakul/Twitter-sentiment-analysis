#!/usr/bin/env python3
import argparse
import numpy as np
import pickle
from preprocessing import preprocess_tweet, get_doc_list
from sklearn.model_selection import train_test_split

def random_precision(X_test, y_test):
    total = 0
    for x, y in zip(X_test, y_test):
        #sentiment = np.random.choice([0,1])
        sentiment = 1
        if sentiment == y:
            total += 1
    return total/len(y_test)

def main(args):
    
    # Load the tokenizer
    tokenizer = pickle.load(args.tokenizer)

    encoded_docs, labels = get_doc_list(args.input, tokenizer)

    # Mix the data
    randomize = np.arange(len(labels))
    np.random.shuffle(randomize)
    encoded_docs = encoded_docs[randomize,:]
    labels = labels[randomize]

    # Split into test/training data
    X_train, X_test, y_train, y_test = \
    train_test_split(encoded_docs, labels, test_size=0.33)

    # Compute the error on the test set
    test_acc = random_precision(X_test, y_test)

    print("Test accuracy:", test_acc)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--tokenizer", \
    type=argparse.FileType("rb"))
    parser.add_argument("--input","-i")
    args = parser.parse_args()
    main(args)

