import click


@click.group()
def cmd():
    """
    Infrared Command line interface.
    :return:
    """
    pass

@click.command()
@click.option('--exec')
def runner():
    """
    Execute given command from cli.
    :return:
    """
    pass

@click.command()
@click.option('--install_plugins')
@click.argument('plugin_name')
def install_plugin(plugin_name):
    """
     Install plugin.
    :return: parser object
    """
    click.echo('Installing plugins: {}'.format(plugin_name))

@click.command()
@click.option('--list-plugins')
def list_plugins(key=None, repo_path=None):
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

@click.command()
@click.option('--list-all-plugins')
def list_installed_plugins(plugin_path=None):
    """
    List locally installed plugins which will have precidence over
    list_plugin method.
    :param plugin_path: local directory path.
    :return: list of installed plugins or available plugins for install.
    """
    pass

@click.command()
@click.option('--remove')
def remove_plugin():
    """
    Remove or uninstall given plugin by name.
    :return:
    """
    pass

command_list = [runner, install_plugin, list_plugins, list_installed_plugins, remove_plugin]

for cmd_element in command_list:
    cmd.add_command(cmd_element)
