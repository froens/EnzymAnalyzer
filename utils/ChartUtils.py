"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""
import numpy as np
import matplotlib.pyplot as plt


def showchart(title, feature, targets, target_labels):

    N = len(feature)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.15       # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, feature, width, color='r')
    rects2 = ax.bar(ind + width, targets, width, color='g')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Scores')
    ax.set_title(title)
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(target_labels)

    ax.legend((rects1[0], rects2[0]), ('Feature measurements', 'Targets'))


    def autolabel(rects):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%f' % int(height),
                    ha='center', va='bottom')



    plt.show()