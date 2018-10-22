#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:13:11 2018

@author: itt-mcc
"""

from sklearn.cluster import DBSCAN
from scipy.spatial import distance
from scipy.optimize import curve_fit
import numpy as np, math
data = [[331, 400], [331, 1200], [332, 400], [332, 486], [332, 522]] #....

def angle(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    inner_product = x1*x2 + y1*y2
    len1 = math.hypot(x1, y1)
    len2 = math.hypot(x2, y2)
    return math.acos(inner_product/(len1*len2))

db=DBSCAN(eps=1,min_samples=2,metric='precomputed').fit(
  distance.squareform(distance.pdist(data)))
core_samples = db.core_sample_indices_
labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
unique_labels = set(labels)

for k in unique_labels:
    class_members = [index[0] for index in np.argwhere(labels == k)]
    cluster_core_samples = [index for index in core_samples
                            if labels[index] == k]
    curve = np.array([data[index] for index in class_members])
    print(k, curve, [angle(p1,p2) for p1,p2 in zip(curve,curve[1:])])