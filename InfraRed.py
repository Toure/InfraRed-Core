from cli import ConfigManager
from cli.logger import make_timestamped_filename
from cli.logger import glob_logger
import readline
import atexit


class InfraRed(ConfigManager):
    def __init__(self):
        super(InfraRed, self).__init__()
        self.log_dir_path = self.cfg_manager('log_dir')

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
    cfg = ConfigManager()
    cfg.create_parser()
    atexit.register(infraread.save_results)
