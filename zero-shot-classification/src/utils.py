import datetime
import logging
import ntpath
import os
from typing import Optional


def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Directory created: " + directory)
    else:
        print("Directory exists: " + directory)


def create_logger(
    project_name: str,
    level: str = "INFO",
    log_dir: str = "/tmp/logs",
    file_name: Optional[str] = None,
    do_print: bool = True,
    simple_logging: bool = False,
    log_to_file: bool = False,
    rich_logging: bool = False,
    time_zone: Optional[str] = None,
):
    """Creates a logger of given level and saves logs to a file

    :param project_name: project name for which we are logging
    :param level: logging level
                  LEVELS available
                  DEBUG: Detailed information, typically of interest only when diagnosing problems.
                  INFO: Confirmation that things are working as expected.
                  WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
                  ERROR: Due to a more serious problem, the software has not been able to perform some function.
                  CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
    :param log_dir: directory when log files are created
    :param file_name: name of the log file
    :param do_print: whether to print the logs
    :param simple_logging: sets formatter to only message
    :param log_to_file: whether to save logs on disk
    :param rich_logging: colorful logging using rich
    :param time_zone: timezone to be used for time in logging such as Asia/Kolkata
                      https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
    """
    import __main__

    if file_name is None:
        try:
            file_name = ntpath.basename(__main__.__file__).split(".")[0]
        except:
            file_name = "logs"

    logger = logging.getLogger(file_name)
    logger.handlers.clear()
    logger.setLevel(getattr(logging, level))

    if time_zone:
        from pytz import timezone, utc
        def time_formatter(*args):
            # TODO: Doesnt work with rich formatter
            utc_dt = utc.localize(datetime.datetime.utcnow())
            my_tz = timezone(time_zone)
            converted = utc_dt.astimezone(my_tz)
            return converted.timetuple()

        logging.Formatter.converter = time_formatter

    if rich_logging:
        from rich.logging import RichHandler
        stream_format = f"{project_name}:%(module)s:%(funcName)s: %(message)s"
        stream_handler = RichHandler(omit_repeated_times=False)
    else:
        stream_format = f"%(asctime)s:%(levelname)s:{project_name}:%(module)s:%(funcName)s: %(message)s"
        stream_handler = logging.StreamHandler()

    file_formatter = stream_formatter = logging.Formatter(
        stream_format, "%Y-%m-%d %H:%M:%S"
    )

    if simple_logging:
        file_formatter = logging.Formatter("%(message)s")
        stream_formatter = logging.Formatter("%(message)s")

    if log_to_file:
        date = datetime.date.today()
        date = "%s-%s-%s" % (date.day, date.month, date.year)
        log_file_path = os.path.join(log_dir, "%s-%s.log" % (file_name, date))

        create_folder(log_dir)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    if do_print:
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)

    logger.propagate = False

    return logger
