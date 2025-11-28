# Visuals
#
# python -m src.visuals


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


from src.config import IMAGES_FOLDER


def heatmap(data, plt_show=True):
    """
    Heatmap visualization.

    Parameters:
        data: Data
        plt_show: If True the plot will be shown. Otherwise the plot will be saved in IMAGES_FOLDER

    Returns:
        None
    """
    sns.heatmap(data, cmap="Blues", cbar=False)

    if plt_show is True:
        plt.show()
    else:
        output_image_path = IMAGES_FOLDER

        output_image_path = output_image_path + "heatmap.png"

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
    plt.bar(labels, values)
    plt.xticks(rotation=45)

    if plt_show is True:
        plt.show()
    else:
        output_image_path = IMAGES_FOLDER

        output_image_path = output_image_path + "histogram.png"

        plt.savefig(output_image_path)


# def word_cloud(labels, values, plt_show=True):
#     """
#     Histogram visualization.

#     Parameters:
#         labels: Labels
#         values: Values
#         plt_show: If True the plot will be shown. Otherwise the plot will be saved in IMAGES_FOLDER

#     Returns:
#         None
#     """
#     plt.bar(labels, values)
#     plt.xticks(rotation=45)

#     if plt_show is True:
#         plt.show()
#     else:
#         output_image_path = conf.IMAGES_FOLDER

#         output_image_path = output_image_path + 'histogram.png'

#         plt.savefig(output_image_path)

#     f = plt.figure(figsize = (20, 10))
#     f.suptitle(neighborhood)
#     ax = f.add_subplot(121)
#     ax2 = f.add_subplot(122)

#     ax.set_title('listing_neighborhood_overview')
#     ax.axis("off")

#     ax2.set_title('review_contextual_phrases')
#     ax2.axis("off")

#     try:
#         wordcloud_neighborhood_overview = WordCloud(stopwords=stop_words).generate(string_list_neighborhood_overview)
#         ax.imshow(wordcloud_neighborhood_overview, interpolation='bilinear')

#         wordcloud_contextual_phrases = WordCloud(stopwords=stop_words).generate(string_list_contextual_phrases)
#         ax2.imshow(wordcloud_contextual_phrases, interpolation='bilinear')
#     except:
#         pass
#     TODO


if __name__ == "__main__":
    print("Visuals")

    test_data_heatmap = np.random.rand(10, 10)
    heatmap(test_data_heatmap, plt_show=False)

    test_labels_histogram = ["A", "B", "C", "D", "E"]
    test_values_histogram = [5, 7, 3, 8, 6]
    histogram(test_labels_histogram, test_values_histogram, plt_show=False)
else:
    pass
