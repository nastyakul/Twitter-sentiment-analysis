#!/usr/bin/env python3
import argparse
import numpy as np
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from preprocessing import get_doc_list

def main(args):

    # Load the tokenizer
    tokenizer = pickle.load(args.tokenizer)

    encoded_docs, labels = get_doc_list(args.input, tokenizer)

    # Create the model
    model = MultinomialNB()

    # Split into test/training data
    X_train, X_test, y_train, y_test = \
    train_test_split(encoded_docs, labels, test_size=0.33)

    # Train
    model.fit(X_train, y_train)

    # Compute the error on the test set
    test_acc = model.score(X_test, y_test)

    print("Test accuracy:", test_acc)

    # Save the model
    pickle.dump(model, args.model)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=argparse.FileType("wb"))
    parser.add_argument("--tokenizer", \
    type=argparse.FileType("rb"))
    parser.add_argument("--input","-i")
    args = parser.parse_args()
    main(args)



