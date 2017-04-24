import numpy as np


def get_labels(target_dict, target_order, threshold):
    targets = np.zeros((len(target_order)))
    for key_i, key in enumerate(target_order):

        targets[key_i] = 1 if target_dict[key] > threshold else 0

    return targets


def transpose_data(data):

    old_keys = [key for key in data[0]]

    result = []
    for ok in old_keys:
        new_row = dict()
        new_row['measurement_point'] = ok

        old_column = [(x['SEQUENCE ID'], x[ok]) for x in data]
        for nk, val in old_column:
            new_row[nk] = val

        result.append(new_row)

    return result


def extract_features(data):
    measurements = sorted([x for x in data if x['measurement_point'].startswith("ROA_")], key=lambda k: k['measurement_point'])
    sequence_ids = sorted([key for key in data[0] if key.startswith("roa_")])
    measurement_ids = [x['measurement_point'] for x in measurements]

    #  if "ROA_" in key
    row_num = len(measurements)
    column_num = len(sequence_ids)
    result = np.zeros((row_num, column_num))

    for measurement_i, measurement in enumerate(measurements):
        for seq_i, seq_key in enumerate(sequence_ids):
            result[measurement_i, seq_i] = measurements[measurement_i][seq_key]
    return result, sequence_ids, measurement_ids

