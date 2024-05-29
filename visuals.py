# Visuals
#
# python visuals.py


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import seaborn as sns


import configuration


def heatmap(data, plt_show=True):
    """
    Heatmap visualization.

    Parameters:
        data: Data
        plt_show: If True the plot will be shown. Otherwise the plot will be saved in IMAGES_FOLDER

    Returns:
        None
    """
    fig = plt.figure(figsize = (22, 22))
    
    sns.heatmap(data, cmap = 'Blues', cbar = False)

    if plt_show is True:
        plt.show()
    else:
        output_image_path = configuration.IMAGES_FOLDER

        output_image_path = output_image_path + 'heatmap.png'

        plt.savefig(output_image_path)


def histogram(labels, values, plt_show=True):
    """
    Histogram visualization.

    Parameters:
        labels: Labels
        values: Values
        plt_show: If True the plot will be shown. Otherwise the plot will be saved in IMAGES_FOLDER

    Returns:
        None
    """
    fig = plt.figure(figsize = (20, 10)) 
    plt.bar(labels, values)
    plt.xticks(rotation=90)

    if plt_show is True:
        plt.show()
    else:
        output_image_path = configuration.IMAGES_FOLDER

        output_image_path = output_image_path + 'histogram.png'

        plt.savefig(output_image_path)


if __name__ == '__main__':
    print('Visuals')

    test_data_heatmap = np.random.rand(10, 10)
    heatmap(test_data_heatmap, plt_show=False)

    test_labels_histogram = ['A', 'B', 'C', 'D', 'E']
    test_values_histogram = [5, 7, 3, 8, 6]
    histogram(test_labels_histogram, test_values_histogram, plt_show=False)
else:
    pass
