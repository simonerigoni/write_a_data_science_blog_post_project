# Test conf
#
# python test_conf.py

import os
import shutil


import src.config as conf


def test_create_folders():
    test_folder = "test_folder"
    if not os.path.exists(test_folder):
        pass
    else:
        shutil.rmtree(test_folder)

    conf.create_folders(test_folder)
    test_result = os.path.exists(test_folder)
    shutil.rmtree(test_folder)
    assert test_result
