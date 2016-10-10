import clg
import os
import yaml
import yamlordereddictloader

from configmanager import lookup
from configmanager import CURRENT_DIR

CORE_ARGS_FILE = os.path.join(CURRENT_DIR, "../configs/core_args.yml")


def install_plugin(plugin_name):
    """
     Install plugin.
    :return: parser object
    """
    print("{}".format(plugin_name))


def install_all_plugins():
    """
    Install all available plugins.
    :return:
    """
    pass


def list_plugins(value, key=None, repo_path=None):
    """
    List plugins will display all available core plugins.
    :return:
    """

    plugin_list = None

    if repo_path is None:
        plugin_list = lookup('repos')
    else:
        try:
            plugin_list = lookup(key, repo_path)
        except ValueError:
            print("Could not find given plugin: {}".format(key))

    print("Available plugin for install:")
    for k, _ in plugin_list.items():
        print(k)


def list_installed_plugins(value):
    """
    List locally installed plugins which will have precidence over
    list_plugin method.
    :param plugin_path: local directory path.
    :return: list of installed plugins or available plugins for install.
    """
    pass


def remove_plugin():
    """
    Remove or uninstall given plugin by name.
    :return:
    """
    pass

clg.TYPES.update({
    'install': install_plugin,
    'install_all': install_all_plugins,
    'list': list_plugins,
    'list_installed': list_installed_plugins,
    'remove': remove_plugin,
})


def main():
    cmd = clg.CommandLine(yaml.load(open(CORE_ARGS_FILE),
                                    Loader=yamlordereddictloader.Loader))
    return cmd.parse()

if __name__ == '__main__':
    main()
