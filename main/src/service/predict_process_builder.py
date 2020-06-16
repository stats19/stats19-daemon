from dataclasses import dataclass
from typing import Dict, Any

from main.src.exporter.broker_exporter import BrokerExporter
from main.src.importer.api_importer import ApiImporter
from main.src.importer.broker_importer import BrokerImporter
from main.src.process.predict_process import PredictProcess
from main.src.service.builder import ApiSourceBuilder, BrokerSourceBuilder, BrokerDestinationBuilder


@dataclass
class PredictProcessBuilder:
    source_config_api: Dict[Any, Any]
    process_config: Dict[Any, Any]
    source_config_broker: Dict[Any, Any]
    destination_config_broker: Dict[Any, Any]
    force_process_execution: bool

    def build_process(self) -> PredictProcess:
        importer_api = self._build_impoter_api()
        importer_broker = self._build_impoter_broker()
        exporter_broker = self._build_exporter_broker()
        return PredictProcess(name=self.process_config['name'],
                              use_asyncio=False,
                              force_process_execution=self.force_process_execution,
                              importer_api=importer_api,
                              importer_broker=importer_broker,
                              exporter_broker=exporter_broker
                              )

    def _build_impoter_api(self) -> ApiImporter:
        builder = ApiSourceBuilder(self.source_config_api)
        return builder.build_importer()

    def _build_impoter_broker(self) -> BrokerImporter:
        builder = BrokerSourceBuilder(self.source_config_broker)
        return builder.build_importer()

    def _build_exporter_broker(self) -> BrokerExporter:
        builder = BrokerDestinationBuilder(self.destination_config_broker)
        return builder.build_exporter()
