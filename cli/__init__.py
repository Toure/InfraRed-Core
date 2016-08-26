import argparse
import os
import yaml
import sys

CURRENT_DIR = os.path.dirname(__file__)
CONF = os.path.join(CURRENT_DIR, "./InfraRed.yaml")


class Cli(object):
    """
    CLi class.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Logic found here will insure a single instance of values are being used
        throughout the project.
        """
        if not cls._instance:
            cls._instance = super(Cli, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @staticmethod
    def create_parser():
        """
        Create parser will return a parser object.
        :return:
        """
        parser = argparse.ArgumentParser(description="InfraRed command line interface.")
        parser.add_argument("-r", "--repo", dest="repo",
                            help="Name of functionality which should be imported."
                                 "Example: -r installer")
        parser.add_argument("-i", "--inventory", dest="inventory",
                            help="List of hostname which will be passed to ansible.")
        parser.add_argument("-u", "--repo-url", dest="repo-url",
                            help="Custom url for alternative repos.")
        parser.add_argument("-f", "--filename", dest="fname",
                            help="Name of file which artifacts will be recorded.")

        if len(sys.argv) == 1:
            parser.print_help()
            exit(1)
        else:
            return parser.parse_args()


class ConfigManager(Cli):
    def __init__(self):
        super(ConfigManager, self).__init__()
        self.args = self.create_parser()

    def cfg_manager(self, key, collection=CONF):
        """
        Config manager will search configurations file and cli for a given key and give precedence to the non-Null
        value from the cli.
        :param collection: yaml file which contains configuration data.
        :param key: search value to lookup in yaml structure.
        :return: value of corresponding key.
        """
        coll = self.dump_config(collection)
        config_value = self.lookup(coll, key)
        cli_value = self.lookup(vars(self.args), key)

        if cli_value is not None:
            return cli_value
        else:
            return config_value

    def lookup(self, config_dict, search_key):
        """
        lookup will search the given collection for a specified key and return
        its value.
        :param search_key: key in specified collection.
        :param config_dict: dictionary which contains the search key.
        :return: value of search_key.
        """
        if search_key in config_dict:
            return config_dict[search_key]
        for k, v in config_dict.items():
            if isinstance(v, dict):
                item = self.lookup(v, search_key)
                if item is not None:
                    return item

    @staticmethod
    def dump_config(config_obj):
        with open(config_obj, 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as ye:
                print(ye)

    def update_config(self, config_dict):
        """
        Update cli will write persistent values to cli file.
        :param config_dict: map which contain values for permanent record.
        :return: None
        """
        pass

    @staticmethod
    def write_config(config_dict, fname):
        """
        Write cli will dump the above yaml defaults into the users .cli/Iridium directory.
        :param config_dict: name of the map which will be dumped as a yaml file.
        :param fname: name of output yaml file.
        :return: cli.yaml
        """
        with open(fname, "w") as cfg_stream:
            yaml.dump(config_dict, cfg_stream)
            cfg_stream.write("\n")
        cfg_stream.close()