#!/usr/bin/env python3
""" Trains a multi layer perceptron """
import argparse
import numpy as np
import pickle
from preprocessing import preprocess_tweet, get_doc_list
from keras.models import Sequential
from keras.layers import Embedding, Dense, Dropout
from sklearn.model_selection import train_test_split

def main(args):
    
    # Load the tokenizer
    tokenizer = pickle.load(args.tokenizer)

    encoded_docs, labels = get_doc_list(args.input, tokenizer)

    # Create the keras model
    model = Sequential()
    model.add(Dense(50,\
    input_shape=(encoded_docs.shape[1],), activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(2, activation="softmax"))
    model.compile(optimizer="adam", \
    loss='sparse_categorical_crossentropy',\
    metrics=['accuracy'])

    # Mix the data
    randomize = np.arange(len(labels))
    np.random.shuffle(randomize)
    encoded_docs = encoded_docs[randomize,:]
    labels = labels[randomize]

    # Split into test/training data
    X_train, X_test, y_train, y_test = \
    train_test_split(encoded_docs, labels, test_size=0.33)

    # Train
    model.fit(X_train, y_train, epochs=5)

    # Compute the error on the test set
    test_loss, test_acc = model.evaluate(X_test, y_test)

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
