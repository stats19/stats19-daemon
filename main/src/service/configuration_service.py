import json
from dataclasses import dataclass
from enum import Enum
from importlib import resources
from typing import Dict, Any

import main.resources.configuration as config_folder


class Configuration(Enum):
    FOLDER = config_folder


@dataclass
class ConfigurationLoaderService(object):
    configuration: Configuration

    def load_process_configuration_file(self, file_name: str) -> Dict[Any, Any]:
        return self.__load_configuration(file_name)

    def __load_configuration(self, file_name: str) -> Dict[Any, Any]:
        folder = self.configuration.value
        with resources.open_text(folder, file_name) as f:
            return json.loads(f.read())
