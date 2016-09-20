import argparse
import sys

from infrared.core.importer import Importer
from inspector import ConfigManager

from infrared.core.exceptions import IRFileNotFoundException

configmanager = ConfigManager()
importer = Importer()


class Cli(object):
    def __init__(self, configmanager_cls, importer_cls):
        super(Cli, self).__init__()
        self.lookup = configmanager_cls.lookup()
        self.search_repo = importer_cls.search_repo()

    def runner(self):
        """
        Execute given command from cli.
        :return:
        """
        pass

    def load_plugins(self):
        """
        Load plugin will load specs file and return new parser object.
        :return: parser object
        """
        plugin_name = args.plugin
        plugin_path = self.lookup(plugin_name)

        try:
            self.search_repos(plugin_name, plugin_path)
        except IRFileNotFoundException(plugin_path):
            print("Could not find given plugin: {}".format(plugin_name))

    def list_plugins(self, key=None, repo_path=None):
        """
        List plugins will display all available core plugins.
        :return:
        """
        plugin_list = None

        if repo_path is None:
            plugin_list = self.lookup('repos')
        else:
            try:
                plugin_list = self.lookup(key, repo_path)
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

    def remove_plugin(self):
        """
        Remove or uninstall given plugin by name.
        :return:
        """
        pass

def cmd_launcher(function_name):
    """
    Command launcher will translate the request from Argparser and call the
    matching method.
    :param function_name:
    :return:
    """
    if function_name == "list_plugin": return cli.list_plugins()
    if function_name == "install_all": return cli.



# Parser
cli = Cli(configmanager, importer)
#
parser = argparse.ArgumentParser(description="InfraRed command line interface.")
parser.add_argument("-l", "--list_plugins", type=cmd_launcher('list_plugin'),
                    help="List all know plugins, based on repo information.")
parser.add_argument('-a', '--install-all-plugins', type=cmd_launcher('install_all'),
                    help="Install all core plugins.")
parser.add_argument("-r" "--remove_plugin", type=cmd_launcher('remove_plugin'),
                    help="Uninstall a given plugin.")
parser.add_argument("-p", "--plugin", dest="plugin",
                    help="Name of plugin which should be installed."
                         "Example: -p provisioner")
parser.add_argument("-u", "--repo-url", dest="repo-url",
                    help="Custom url for alternative repos.")
parser.add_argument("-o", "--outputfile", dest="fname",
                    help="Name of file which artifacts will be recorded.")

args = parser.parse_args()