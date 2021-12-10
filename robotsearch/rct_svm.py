"""
the Randomized Control Trial (RCT) robot predicts whether a given
*abstract* (not full-text) describes an RCT.

This model was trained on the Cochrane crowd dataset, and validated on the Clinical Hedges dataset
"""

# Authors:  Iain Marshall <mail@ijmarshall.com>
#           Joel Kuiper <me@joelkuiper.com>
#           Byron Wallce <byron.wallace@utexas.edu>

import os

import robotsearch
from robotsearch.ml.classifier import MiniClassifier
from sklearn.feature_extraction.text import HashingVectorizer

from scipy.sparse import lil_matrix, hstack



class RCTSVM:
    # changes the cut-off for predicting True
    thresholds = {
        "precise": 1.9237300404146498,
        "sensitive": 0.0691768267655864,
        "balanced": 1.1214599554550992,
    }
    # rescaling for some reason (why isn't this included in threshold?)
    scales = {
         "mean":-0.7548140352548589,
         "std":0.7812955939364481,
         "weight":1.0
      }
    def __init__(self, filter_type):
        self.svm_clf = MiniClassifier(os.path.join(robotsearch.DATA_ROOT, 'rct_svm_weights.npz'))
        self.svm_vectorizer = HashingVectorizer(binary=False, ngram_range=(1, 1), stop_words='english')
        self.threshold = self.thresholds[filter_type]

    def predict(self, X):
        X_title_string = [title for (title, abstract) in X]
        X_title_abstract_string = [f'{title}\n\n{abstract}' for (title, abstract) in X]

        X_title = lil_matrix(self.svm_vectorizer.transform(X_title_string))
        X_title_abstract = lil_matrix(self.svm_vectorizer.transform(X_title_abstract_string))
        svm_scores = self.svm_clf.decision_function(hstack([X_title_abstract, X_title]))
        svm_scores_scaled = (svm_scores - self.scales['mean']) / self.scales['std']
        predictions = (svm_scores_scaled >= self.threshold)
        return predictions
