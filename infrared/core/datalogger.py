"""
DataLogger will save data to a store of a sort. ex: database, file.
"""


class DataLogger(object):
    """
    DataLogger will accept a data stream and write it to file or database.
    """
    def save_log(self, user_id, log_handle, runtime, task_status):
        """
        Save logs will record task run information.
        :param user_id: user id information running the ansible task.
        :param log_handle: the ansible playlogger handle which contains information
                           about the task.
        :param runtime: total elapse time.
        :param task_status: status of the run passed or failed.
        :return: None.
        """
        pass