"""
the Randomized Control Trial (RCT) robot predicts whether a given
*abstract* (not full-text) describes an RCT.

    title =    '''Does usage of a parachute in contrast to free fall prevent major trauma?: a prospective randomised-controlled trial in rag dolls.'''
    abstract = '''PURPOSE: It is undisputed for more than 200 years that the use of a parachute prevents major trauma when falling from a great height. Nevertheless up to date no prospective randomised controlled trial has proven the superiority in preventing trauma when falling from a great height instead of a free fall. The aim of this prospective randomised controlled trial was to prove the effectiveness of a parachute when falling from great height. METHODS: In this prospective randomised-controlled trial a commercially acquirable rag doll was prepared for the purposes of the study design as in accordance to the Declaration of Helsinki, the participation of human beings in this trial was impossible. Twenty-five falls were performed with a parachute compatible to the height and weight of the doll. In the control group, another 25 falls were realised without a parachute. The main outcome measures were the rate of head injury; cervical, thoracic, lumbar, and pelvic fractures; and pneumothoraxes, hepatic, spleen, and bladder injuries in the control and parachute groups. An interdisciplinary team consisting of a specialised trauma surgeon, two neurosurgeons, and a coroner examined the rag doll for injuries. Additionally, whole-body computed tomography scans were performed to identify the injuries. RESULTS: All 50 falls-25 with the use of a parachute, 25 without a parachute-were successfully performed. Head injuries (right hemisphere p = 0.008, left hemisphere p = 0.004), cervical trauma (p < 0.001), thoracic trauma (p < 0.001), lumbar trauma (p < 0.001), pelvic trauma (p < 0.001), and hepatic, spleen, and bladder injures (p < 0.001) occurred more often in the control group. Only the pneumothoraxes showed no statistically significant difference between the control and parachute groups. CONCLUSIONS: A parachute is an effective tool to prevent major trauma when falling from a great height.'''
    ptyp = ["Randomized Controlled Trial", "Intervention Study", "Journal Article"]

    rct_robot = RCTRobot()
    annotations = rct_robot.annotate(title, abstract, ptyp)

This model was trained on the Cochrane crowd dataset, and validated on the Clinical Hedges dataset
"""

# Authors:  Iain Marshall <mail@ijmarshall.com>
#           Joel Kuiper <me@joelkuiper.com>
#           Byron Wallce <byron.wallace@utexas.edu>

import json
import uuid
import os

import pickle

import robotsearch
from robotsearch.ml.classifier import MiniClassifier
from sklearn.feature_extraction.text import HashingVectorizer
from robotsearch.parsers import ris

from scipy.sparse import lil_matrix, hstack

import numpy as np
import re
import glob
from sklearn.base import ClassifierMixin
from collections import Counter

from typing import Any

class RCTRobot:

    def __init__(self):
        import time
        tic = time.perf_counter()
        self.svm_clf = MiniClassifier(os.path.join(robotsearch.DATA_ROOT, 'rct/rct_svm_weights.npz'))
        self.svm_vectorizer = HashingVectorizer(binary=False, ngram_range=(1, 1), stop_words='english')
        with open(os.path.join(robotsearch.DATA_ROOT, 'rct/rct_model_calibration.json'), 'r') as f:
            self.constants = json.load(f)
        toc = time.perf_counter()
        print(f'Loading SVM and vectorizer and stuff took {toc - tic:0.4f}')

    def predict(self, X: list[tuple[str, str]], filter_class="svm", filter_type="sensitive", raw_scores=False) -> dict[str, Any]:
        preds_l = {}

        # thresholds vary per article
        thresholds = []
        for r in X:
            thresholds.append(self.constants['thresholds'][filter_class][filter_type])

        X_ti_str = [pair[0] for pair in X]
        X_ab_str = [f'{pair[0]}\n\n{pair[1]}' for pair in X]

        svm_preds = None
        if "svm" in filter_class:
            X_ti = lil_matrix(self.svm_vectorizer.transform(X_ti_str))
            X_ab = lil_matrix(self.svm_vectorizer.transform(X_ab_str))
            svm_preds = self.svm_clf.decision_function(hstack([X_ab, X_ti]))
            svm_scale =  (svm_preds - self.constants['scales']['svm']['mean']) / self.constants['scales']['svm']['std']
            preds_l['svm'] = svm_scale


        preds_d =[dict(zip(preds_l,i)) for i in zip(*preds_l.values())]

        out = []

        if raw_scores:
            return {
                    "svms": svm_preds,
                    }

        else:
            for pred, threshold in zip(preds_d, thresholds):
                row = {}
                row['model'] = filter_class
                row['score'] = float(pred[row['model']])
                row['threshold_type'] = filter_type
                row['threshold_value'] = float(threshold)
                row['is_rct'] = bool(row['score'] >= threshold)
                row['preds'] = {k: float(v) for k, v in pred.items()}
                out.append(row)
            return out


