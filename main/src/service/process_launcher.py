import logging
from dataclasses import dataclass, field
from typing import Dict, Any, Callable

from main.src.process.broker_process import BrokerProcess
from main.src.process.leagues_process import LeaguesProcess
from main.src.process.create_model_process import CreateModelProcess
from main.src.process.predict_process import PredictProcess
from main.src.process.process_interface import Process
from main.src.process.score_process import ScoreProcess
from main.src.service.broker_process_builder import BrokerProcessBuilder
from main.src.service.configuration_service import Environment, ConfigurationLoaderService
from main.src.service.create_model_process_builder import CreateModelProcessBuilder
from main.src.service.leagues_process_builder import LeaguesProcessBuilder
from main.src.service.predict_process_builder import PredictProcessBuilder
from main.src.service.score_process_builder import ScoreProcessBuilder
from main.src.utils.utils import extract_dict_value

logger = logging.getLogger(__name__)

process_name_2_configuration_file = {
    'leagues': 'config-leagues.json',
    'createModel': 'config-create_model.json',
    'predict': 'config-predict.json',
    'broker': 'config-broker.json',
    'score': 'config-scores.json'
}


@dataclass
class ProcessLauncher(object):
    environment: Environment
    force_process_execution: bool
    process_name: str
    process: Process = field(init=False)
    process_name_2_builder_function: Dict[str, Callable[[Dict[Any, Any]], Process]] = field(init=False)

    def __post_init__(self):
        self.process_name_2_builder_function = {
            'leagues': self.build_leagues_process,
            'createModel': self.build_create_model_process,
            'predict': self.build_predict_process,
            'broker': self.build_broker_process,
            'score': self.build_score_process
        }

    def build_process(self):
        logger.info('Start building process')
        logger.info('Load data from configuration file')

        try:
            configuration_loader = ConfigurationLoaderService(self.environment)
            file_name = process_name_2_configuration_file[self.process_name]

            configuration_file = configuration_loader.load_process_configuration_file(file_name)
            builder_function = self.process_name_2_builder_function[self.process_name]

            self.process = builder_function(configuration_file)

        except(TypeError, KeyError) as e:
            logger.fatal(f'An error occured when parsing configuration file for process {self.process_name}')
            logger.fatal(e)

    def build_leagues_process(self, configuration_file: Dict[Any, Any]) -> LeaguesProcess:
        process_name = extract_dict_value(configuration_file, lambda dict_: dict_['process']['name'])

        logger.info(f'Build process {process_name}')

        source_api_config = configuration_file['sources']['api']

        process_config = configuration_file['process']

        leagues_process_builder = LeaguesProcessBuilder(force_process_execution=self.force_process_execution,
                                                        process_config=process_config,
                                                        source_config_api=source_api_config)
        return leagues_process_builder.build_process()

    def build_score_process(self, configuration_file: Dict[Any, Any]) -> ScoreProcess:
        process_name = extract_dict_value(configuration_file, lambda dict_: dict_['process']['name'])

        logger.info(f'Build process {process_name}')

        source_api_config = configuration_file['sources']['api']

        process_config = configuration_file['process']

        score_process_builder = ScoreProcessBuilder(force_process_execution=self.force_process_execution,
                                                    process_config=process_config,
                                                    source_config_api=source_api_config)
        return score_process_builder.build_process()

    def build_create_model_process(self, configuration_file: Dict[Any, Any]) -> CreateModelProcess:
        process_name = extract_dict_value(configuration_file, lambda dict_: dict_['process']['name'])

        logger.info(f'Build process {process_name}')

        source_api_config = configuration_file['sources']['api']

        process_config = configuration_file['process']

        predict_process_builder = CreateModelProcessBuilder(force_process_execution=self.force_process_execution,
                                                            process_config=process_config,
                                                            source_config_api=source_api_config)
        return predict_process_builder.build_process()

    def build_predict_process(self, configuration_file: Dict[Any, Any]) -> PredictProcess:
        process_name = extract_dict_value(configuration_file, lambda dict_: dict_['process']['name'])

        logger.info(f'Build process {process_name}')

        source_api_config = configuration_file['sources']['api']

        process_config = configuration_file['process']

        predict_process_builder = PredictProcessBuilder(force_process_execution=self.force_process_execution,
                                                        process_config=process_config,
                                                        source_config_api=source_api_config)
        return predict_process_builder.build_process()

    def build_broker_process(self, configuration_file: Dict[Any, Any]) -> BrokerProcess:
        process_name = extract_dict_value(configuration_file, lambda dict_: dict_['process']['name'])

        logger.info(f'Build process {process_name}')

        source_config_broker = configuration_file['sources']['broker']
        destination_config_broker = configuration_file['destinations']['broker']

        process_config = configuration_file['process']

        broker_process_builder = BrokerProcessBuilder(force_process_execution=self.force_process_execution,
                                                      process_config=process_config,
                                                      source_config_broker=source_config_broker,
                                                      destination_config_broker=destination_config_broker)
        return broker_process_builder.build_process()

    def start(self) -> None:
        if self.process is not None:
            self.process.call_process()

    async def async_start(self) -> None:
        if self.process is not None:
            await self.process.call_process()
