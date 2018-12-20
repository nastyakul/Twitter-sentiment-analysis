#!/usr/bin/env python3
import numpy as np
from sklearn.metrics import recall_score, precision_score, f1_score

def evaluate(X_test, y_test, y_pred):

    # Turn the prediction into round numbers
    y_pred = np.round(y_pred)
    
    recall_leave = recall_score(y_test, y_pred, pos_label = 1)
    precision_leave = precision_score(y_test, y_pred,\
    pos_label = 1)

    recall_stay = recall_score(y_test, y_pred, pos_label = 0)
    precision_stay = precision_score(y_test, y_pred,\
    pos_label = 0)

    print("Recall Leave:", recall_leave)
    print("Precision Leave:", precision_leave)
    print("Recall Stay:", recall_stay)
    print("Precision Stay:", precision_stay)

