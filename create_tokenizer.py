#!/usr/bin/env python3
""" Handles the creation and parametrization of the tokenizer object , used to convert text into a vector """
from keras.preprocessing.text import Tokenizer
from preprocessing import train_on_docs
import argparse
import pickle

def main(args):
    # Create the tokenizer object
    tokenizer = Tokenizer(num_words=7000, lower = True)

    # Train it
    tokenizer = train_on_docs(args.input, tokenizer)

    # Save the tokenizer
    pickle.dump(tokenizer, args.tokenizer)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input","-i")
    parser.add_argument("--tokenizer", \
    type=argparse.FileType("wb"))
    args = parser.parse_args()
    main(args)
