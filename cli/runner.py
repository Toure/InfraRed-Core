import os
import sys

from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.executor.playbook_executor import PlaybookExecutor

from cli import ConfigManager


class Runner(ConfigManager):
    """
    Runner class will serve as an interface to ansible after collecting information from the
    command line it will launch a given playbook / role.
    """
    def __init__(self, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='local',
                 module_path=None, forks=100, remote_user='stack', private_key_file=None, ssh_common_args=None,
                 ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=False, become_method=None,
                 become_user='root', verbosity=None, check=False, host_list=None):

        super(Runner, self).__init__()
        self.listtags = listtags
        self.listtasks = listtasks
        self.listhosts = listhosts
        self.syntax = syntax
        self.connection = connection
        self.module_path = module_path
        self.forks = forks
        self.remote_user = remote_user
        self.private_key_file = private_key_file
        self.ssh_common_args = ssh_common_args
        self.ssh_extra_args = ssh_extra_args
        self.sftp_extra_args = sftp_extra_args
        self.scp_extra_args = scp_extra_args
        self.become = become
        self.become_method = become_method
        self.become_user = become_user
        self.verbosity = verbosity
        self.check = check
        self.loader = DataLoader()
        self.variable_manger = VariableManager()
        self.host_list = self.args.inventory

    def load_inventory(self):
        """

        :param load_name:
        :return:
        """
        inventory = Inventory(loader=self.loader, variable_manager=self.variable_manger,
                              host_list=self.host_list)
        return inventory

    def run_plays(self, playbook_path):
        """
        Run Play will execute playbooks.
        :param playbook_path:
        :return:
        """
        try:
            os.path.exists(playbook_path)
        except Exception as ex:
            print ("The specified path doesn't exist: {}".format(playbook_path))
            sys.exit()

        self.variable_manger.extra_vars = {
            'hosts': 'localhost'}  # This can accomodate various other command line arguments.`

        passwords = {}
        pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=self.load_inventory(),
                                variable_manager=self.variable_manger, loader=self.loader,
                                options=options, passwords=passwords)
        results = pbex.run()

        return results
