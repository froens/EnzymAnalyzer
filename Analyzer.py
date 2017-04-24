#!/usr/bin/python
import time

from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import MinMaxScaler

from utils import FileUtils as enz_file, PreprocessingUtils as enz_preprocessing, ChartUtils

timestamp = int(time.time())


for i in range(1):
    target_dict = enz_file.load_targets("targets.csv")
    data = enz_file.loaddata("new_data.csv")

    # Filter on PFAM
    data_filtered = [x for x in data if "PF00067" in x["PFAM"]]

    data_transposed = enz_preprocessing.transpose_data(data_filtered)
    enz_file.write_to_csv(data_transposed)
    features, sequence_ids, measurement_ids = enz_preprocessing.extract_features(data_transposed)
    labels = enz_preprocessing.get_labels(target_dict, measurement_ids, 1000)

    scaler = MinMaxScaler()
    features_scaled = scaler.fit_transform(features)
    targets = [target_dict[x] for x in measurement_ids]
    targets_scaled = scaler.fit_transform(targets)

    selector = SelectKBest(chi2, k=5)
    selector.fit(features, labels)
    support = selector.get_support(True)




    # sum_of_squares = []
    # feature_scaled_rows = np.transpose(features_scaled)
    # for f in feature_scaled_rows:
    #
    #    sos = enz_utils.sum_of_squares(f, targets_scaled)
    #    sum_of_squares.append((f,sos))
    # sum_of_squares = sorted(sum_of_squares, key=lambda x: x[1])
    # Chart.showchart("Lowest", sum_of_squares[-1][0], targets_scaled, measurement_ids)
    for s_index in support:
        seq_id = sequence_ids[s_index]
        feature_scaled = features_scaled[:, s_index]
        ChartUtils.showchart(sequence_ids[s_index], feature_scaled, targets_scaled, measurement_ids)
        # sos = enz_utils.sum_of_squares(feature_scaled, targets_scaled)
        print(sequence_ids[s_index], selector.scores_[s_index])
