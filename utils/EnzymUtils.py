#!/usr/bin/python


def sum_of_squares(feature, target):
    sum_of_s = 0
    for m_index, measure in enumerate(feature):
        f = feature[m_index]
        t = target[m_index]
        sum_of_s = sum_of_s + (t-f)**2
    return sum_of_s