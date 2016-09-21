
import os
import yaml

CURRENT_DIR = os.path.dirname(__file__)
CONF = os.path.join(CURRENT_DIR, "../configs/infrared_base_config.yaml")


class SpecManager(object):
    def lookup(self, key, collection=CONF):
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
