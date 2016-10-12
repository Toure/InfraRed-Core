import yaml
import yamlordereddictloader


def yaml_conf(config_name):
    """
    yaml_conf will transform a given yaml file into an ordered dictionary.
    :param config_name: yaml file name to convert.
    :return: ordereddict
    """
    ordered_conf = yaml.load(open(config_name), Loader=yamlordereddictloader.Loader)
    return ordered_conf
