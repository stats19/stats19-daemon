import argparse
import asyncio
import logging
from enum import Enum

from main.src.logger.logger_configuration import setup_logging_configuration
from main.src.service.configuration_service import Environment
from main.src.service.process_launcher import ProcessLauncher

logger = logging.getLogger(__name__)


class ForceLevel(Enum):
    TRUE = True
    FALSE = False


class EnvironmentNotValidException(Exception):
    pass


class ForceNotValidException(Exception):
    pass


def get_force(force_str: str, env_level: Environment) -> bool:
    if force_str == ForceLevel.TRUE.name:
        if env_level == Environment.PRODUCTION:
            logger.warning(f'{force_str} is not a valid force type for environment {env_level}, False returned')
            return ForceLevel.FALSE.value
        else:
            return ForceLevel.TRUE.value
    elif force_str == 'FALSE':
        return ForceLevel.FALSE.value
    else:
        raise ForceNotValidException(f'{force_str} is not a valid force type')


def get_env_level(environment_str: str) -> Environment:
    if environment_str == Environment.DEVELOPMENT.name:
        return Environment.DEVELOPMENT
    elif environment_str == Environment.PRODUCTION.name:
        return Environment.PRODUCTION
    else:
        raise EnvironmentNotValidException


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="Tech Run Collector", usage="report_graph_process.py [options]")
    parser.add_argument("--log_level", default="INFO", help="INFO, DEBUG, WARN or ERROR")
    parser.add_argument("--environment", help="DEVELOPMENT or PRODUCTION")
    parser.add_argument("--processname", help="name of process to execute (defined in configuration file)")
    parser.add_argument("--force", default="FALSE", help="TRUE or FALSE, force the process execution")
    args = parser.parse_args()

    log_level = args.log_level
    environment = args.environment
    process_name = args.processname
    force = args.force

    setup_logging_configuration(log_level, process_name)

    if environment is None:
        logger.fatal('Can not start Application, environment is not definded')
        logger.fatal('DEVELOPMENT or PRODUCTION shall be choosed')
    elif process_name is None:
        logger.fatal('Cannot start application, processname is not defined')
    else:
        logger.info("** Start Server Application**")
        env_level = get_env_level(environment)
        force_level = get_force(force, env_level)

        launcher = ProcessLauncher(process_name=process_name,
                                   force_process_execution=force_level,
                                   environment=env_level)
        launcher.build_process()

    if launcher.process is not None and launcher.process.use_asyncio:
        coroutine = launcher.async_start()
        asyncio.run(coroutine)
    else:
        launcher.start()
