import argparse
import sys
import clg
import yamlordereddictloader


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
        parser.add_argument("-l", "--list_plugins", dest="list_plugins",
                            help="List all know plugins, based on repo information.")
        parser.add_argument("-r" "--remove_plugin", dest="remove_plugin",
                            help="Uninstall a given plugin.")
        parser.add_argument("-p", "--plugin", dest="plugin",
                            help="Name of plugin which should be installed."
                                 "Example: -p provisioner")
        parser.add_argument("-u", "--repo-url", dest="repo-url",
                            help="Custom url for alternative repos.")
        parser.add_argument("-o", "--outputfile", dest="fname",
                            help="Name of file which artifacts will be recorded.")

        if len(sys.argv) == 1:
            parser.print_help()
            exit(1)
        else:
            return parser.parse_args()
