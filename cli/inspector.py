import yaml
import os

from cli import Cli
from cli.importer import Importer
from core.exceptions import IRFileNotFoundException

CURRENT_DIR = os.path.dirname(__file__)
CONF = os.path.join(CURRENT_DIR, "./configs/infrared_base_config.yaml")


class ConfigManager(Cli, Importer):
    def __init__(self):
        super(ConfigManager, self).__init__()
        self.args = self.create_parser()

    def cfg_manager(self, key, collection=CONF):
        """
        Config manager will search configurations file for a given key and return
         its value.
        :param collection: yaml file which contains configuration data.
        :param key: search value to lookup in yaml structure.
        :return: value of corresponding key.
        """
        coll = self._dump_config(collection)
        config_value = self._lookup(coll, key)
        return config_value

    def _lookup(self, config_dict, search_key):
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
                item = self._lookup(v, search_key)
                if item is not None:
                    return item

    @staticmethod
    def _dump_config(config_obj):
        """
        Dump config converts a given yaml file into a filestream.
        :param config_obj: filename which is read.
        :return: returns stream object.
        """
        with open(config_obj, 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as ye:
                print(ye)

    def load_plugins(self):
        """
        Load plugin will load specs file and return new parser object.
        :return: parser object
        """
        plugin_name = self.args.plugin
        plugin_path = self.cfg_manager(plugin_name)

        try:
            self.search_repos(plugin_name, plugin_path)
        except IRFileNotFoundException(plugin_path):
            print("Could not find given plugin: {}".format(plugin_name))

    def list_plugins(self, key=None, repo_path=None):
        """
        List plugins will display all available core plugins.
        :return:
        """
        if repo_path is None:
            plugin_list = self.cfg_manager('repos')
        else:
            try:
                plugin_list = self.cfg_manager(key, repo_path)
            except ValueError:
                print("Could not find given plugin: {}".format(key))

        print("Available plugin for install:")
        for k, _ in plugin_list.items():
            print(k)

    def list_installed_plugins(self, plugin_path=None):
        """
        List locally installed plugins which will have precidence over
        list_plugin method.
        :param plugin_path: local directory path.
        :return: list of installed plugins or available plugins for install.
        """
        pass
