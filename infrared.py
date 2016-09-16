import atexit
import readline

from cli.inspector import ConfigManager
from core.logger import glob_logger
from core.logger import make_timestamped_filename


class InfraRed(ConfigManager):
    def __init__(self):
        super(InfraRed, self).__init__()
        self.log_dir_path = self.cfg_manager('log_dir')

    def load_parser(self):
        """
        Load parser will return parser object to the cli.
        :return: parser object.
        """
        return self.create_parser()

    def runner(self):
        """
        Execute given command from cli.
        :return:
        """
        pass

    def save_results(self):
        """
        Write output to log files.
        :return: timestamped log file.
        """
        glob_logger.info("Saving History...")
        log_path = self.log_dir_path + make_timestamped_filename('iridium_cli_history')
        readline.write_history_file(log_path)


if __name__ == "__main__":
    infraread = InfraRed()
    atexit.register(infraread.save_results)
