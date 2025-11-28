# Test visuals
#
# python test_visuals.py

import os
import numpy as np


from src.config import IMAGES_FOLDER
import src.visuals as vs


def test_heatmapn():
    test_data_heatmap = np.random.rand(10, 10)

    vs.heatmap(test_data_heatmap, plt_show=False)

    output_image_path = IMAGES_FOLDER + "heatmap.png"

    test_result = os.path.exists(output_image_path)
    os.remove(output_image_path)
    assert test_result
