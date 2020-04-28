import argparse
import logging

from main.src.logger.logger_configuration import setup_logging_configuration
from main.src.process.main_process import MainProcess

logger = logging.getLogger(__name__)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="Tech Run Collector", usage="report_graph_process.py [options]")
    parser.add_argument("--log_level", default="INFO", help="INFO, DEBUG, WARN or ERROR")
    args = parser.parse_args()

    log_level = args.log_level

    setup_logging_configuration(log_level)

    logger.info("** Start run Server  **")
    logger.debug('lllo')

    MainProcess.run()


