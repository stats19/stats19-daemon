import argparse
import asyncio
import logging
from enum import Enum

from main.src.logger.logger_configuration import setup_logging_configuration
from main.src.service.configuration_service import Configuration
from main.src.service.process_launcher import ProcessLauncher

logger = logging.getLogger(__name__)


class ForceLevel(Enum):
    TRUE = True,
    FALSE = False


def get_force(force_lvl: str) -> bool:
    if force_lvl == ForceLevel.TRUE.name:
        return ForceLevel.TRUE.value
    return ForceLevel.FALSE.value


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="Tech Run Collector", usage="report_graph_process.py [options]")
    parser.add_argument("--log_level", default="INFO", help="INFO, DEBUG, WARN or ERROR")
    parser.add_argument("--processname", help="name of process to execute (defined in configuration file)")
    parser.add_argument("--force", default="FALSE", help="TRUE or FALSE, force the process execution")
    args = parser.parse_args()

    log_level = args.log_level
    process_name = args.processname
    force = args.force

    setup_logging_configuration(log_level, process_name)

    if process_name is None:
        logger.fatal('Cannot start application, processname is not defined')
    else:
        logger.info("** Start Server Application**")
        force_level = get_force(force)

        launcher = ProcessLauncher(process_name=process_name,
                                   force_process_execution=force_level,
                                   configuration=Configuration.FOLDER)
        launcher.build_process()

    if launcher.process is not None and launcher.process.use_asyncio:
        coroutine = launcher.async_start()
        asyncio.run(coroutine)
    else:
        launcher.start()
