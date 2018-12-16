#!/bin/sh
python label_new.py --model Models/model.p --tokenizer Models/tokenizer.p --input output.jsonl --output Data/labeled_all.jsonl 

