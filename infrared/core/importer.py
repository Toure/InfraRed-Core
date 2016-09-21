from git import Repo

from infrared.core.exceptions import IRException


def clone_repo(repo_url, plugin_path):
    """
    Clone repo will perform the equivalent of git clone <url_of_repo>/repo.git.
    :return: None
    """
    try:
        Repo.clone_from(repo_url, plugin_path)
    except IRException:
        print("Could not retrieve the follow plugin: {}".format(repo_url))


def validate_repo(repo_name):
    """
    Validate repo contains proper structure.
    :param repo_name:
    :return:
    """
    # TODO write a yaml linter.
    pass


def search_repos(repo_name, repo_url):
    """
    Search local and remote for repo_name.
    :param repo_name:
    :return:
    """

    clone_repo(repo_url=repo_url)


def activate_repo(repo_name):
    """
    Activate repo will be called upon removal / uninstallation of repo to keep available
    plugin list in sync.
    :param repo_name: name of repo which was successfully removed.
    :return:
    """
    pass

def deactivate_repo(self, repo_name):
    """
    Deactivate repo will be called to update the status of available
    plugins.
    :param repo_name: name of repo which was successfully installed.
    :return:
    """
    pass

def remove_repo(self, plugin_name):
    """
    Remove repo will uninstall plugin and reset system status for available repos.
    :param repo_name: name of plugin to be removed.
    :return:
    """
    pass
