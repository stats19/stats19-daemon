from dataclasses import dataclass
from typing import Dict, Any

from main.src.importer.api_importer import ApiImporter
from main.src.process.score_process import ScoreProcess
from main.src.service.builder import ApiSourceBuilder


@dataclass
class ScoreProcessBuilder:
    source_config_api: Dict[Any, Any]
    process_config: Dict[Any, Any]
    force_process_execution: bool

    def build_process(self) -> ScoreProcess:
        importer_api = self._build_impoter_api()
        return ScoreProcess(name=self.process_config['name'],
                            use_asyncio=False,
                            force_process_execution=self.force_process_execution,
                            importer_api=importer_api)

    def _build_impoter_api(self) -> ApiImporter:
        builder = ApiSourceBuilder(self.source_config_api)
        return builder.build_importer()
