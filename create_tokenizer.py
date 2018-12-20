#!/usr/bin/env python3
""" Handles the creation and parametrization of the tokenizer object , used to convert text into a vector """

from sklearn.feature_extraction.text import CountVectorizer
from preprocessing import train_on_docs
import argparse
import pickle
import numpy as np

def main(args):
    tokenizer = \
    CountVectorizer(min_df=5, binary=True, \
    ngram_range=(1, args.ngram), dtype=np.bool)

    # Train it
    tokenizer = train_on_docs(args.input, tokenizer)

    print("Vocabulary length:{}".\
    format(len(tokenizer.vocabulary_)))

    # Save the tokenizer
    pickle.dump(tokenizer, args.tokenizer)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input","-i")
    parser.add_argument("--ngram","-n", type=int)
    parser.add_argument("--tokenizer", \
    type=argparse.FileType("wb"))
    args = parser.parse_args()
    main(args)
