from cli import ConfigManager


class Importer(ConfigManager):
    def __init__(self):
        super(Importer, self).__init__()

    def get_repo(self, repo_name):
        """
        Get repo will retrieve given name.
        :return:
        """
        pass

    def validate_repo(self, repo_name):
        """
        Validate repo contains proper structure.
        :param repo_name:
        :return:
        """
        pass
