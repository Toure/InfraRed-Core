import yaml
import yamlordereddictloader
from collections import OrderedDict
import os

CURRENT_DIR = os.path.dirname(__file__)


def yaml_merge(files):
    def merge(dict1, dict2):
        for key, value in dict2.items():
            if key not in dict1:
                dict1[key] = value
            elif isinstance(value, OrderedDict):
                merge(dict1[key], value)

    config = yaml.load(open(files.pop(0)), Loader=yamlordereddictloader.Loader)
    while files:
        merge(config, yaml.load(open(files.pop(0)), Loader=yamlordereddictloader.Loader))
    return config


def yaml_list():
    """
    Yaml list will search current directory and return a list.
    :return:
    """
    files = [os.path.abspath(filename)
             for filename in os.listdir(CURRENT_DIR)
             if os.path.splitext(filename)[-1] in ('.spc', '.spec')]
    return files

