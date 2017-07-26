#!/usr/bin/python
import time

from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.preprocessing import MinMaxScaler
from utils import EnzymUtils as enz_utils
from utils import FileUtils as enz_file, PreprocessingUtils as enz_preprocessing, ChartUtils
import numpy as np

timestamp = int(time.time())


target_dict = enz_file.load_targets("data/Ginkgo_target.csv")
data = enz_file.loaddata("data/Ginkgo_biloba_data.csv")

data_filtered = [x for x in data if 'PF00067' in x["PFAM"]]

"""Transposing of data for MinMax scaling - SelectKBest method for finding best features"""

data_transposed = enz_preprocessing.transpose_data(data_filtered)
enz_file.write_to_csv(data_transposed)
features, sequence_ids, measurement_ids = enz_preprocessing.extract_features(data_transposed)
labels = enz_preprocessing.get_labels(target_dict, measurement_ids, 1000)

scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)
targets = [target_dict[x] for x in measurement_ids]
targets_scaled = scaler.fit_transform(targets)

"""
selector = SelectKBest(f_classif, k=16)
selector.fit(features_scaled, labels)
support = selector.get_support(True)

for s_index in support:
    seq_id = sequence_ids[s_index]
    feature_scaled = features_scaled[:, s_index]
    ChartUtils.showchart(sequence_ids[s_index], feature_scaled, targets_scaled, measurement_ids)
    sos = enz_utils.sum_of_squares(feature_scaled, targets_scaled)
    print(sequence_ids[s_index], selector.scores_[s_index])
"""

sum_of_squares = []
feature_scaled_rows = np.transpose(features_scaled)
for seq_i, f in enumerate(feature_scaled_rows):
    sos = enz_utils.sum_of_squares(f, targets_scaled)
    name = sequence_ids[seq_i]
    sum_of_squares.append((f, sos, name))

sum_of_squares = sorted(sum_of_squares, key=lambda x: x[1])

for s_index in range(10):
    print(sum_of_squares[s_index][2], sum_of_squares[s_index][1])
    print(sum_of_squares[s_index][0])
    ChartUtils.showchart(sum_of_squares[s_index][2], sum_of_squares[s_index][0], targets_scaled, measurement_ids)
