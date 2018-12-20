#!/bin/sh
python label_new.py --model Models/bigram_mlp.p --tokenizer Models/bigram_tokenizer.p --input output.jsonl --output Data/labeled_all.jsonl 

