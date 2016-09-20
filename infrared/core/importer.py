from git import Repo

from infrared.cli.inspector import ConfigManager
from infrared.core.exceptions import IRException
configmanger = ConfigManager()
PLUGIN_PATH = configmanger.lookup('plugin_path')


class Importer(object):
    def clone_repo(self, repo_url):
        """
        Clone repo will perform the equivalent of git clone <url_of_repo>/repo.git.
        :return: None
        """
        try:
            Repo.clone_from(repo_url, PLUGIN_PATH)
        except IRException:
            print("Could not retrieve the follow plugin: {}".format(repo_url))

    def validate_repo(self, repo_name):
        """
        Validate repo contains proper structure.
        :param repo_name:
        :return:
        """
        # TODO write a yaml linter.
        pass

    @classmethod
    def search_repos(self, repo_name, repo_url):
        """
        Search local and remote for repo_name.
        :param repo_name:
        :return:
        """

        self.clone_repo(repo_url=repo_url)

    def activate_repo(self, repo_name):
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