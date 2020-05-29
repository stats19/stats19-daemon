import json
from dataclasses import dataclass
from enum import Enum
from importlib import resources
from typing import Dict, Any

import main.resources.dev as dev_folder
import main.resources.prod as prod_folder


class Environment(Enum):
    DEVELOPMENT = dev_folder
    PRODUCTION = prod_folder


@dataclass
class ConfigurationLoaderService(object):
    environment: Environment

    def load_process_configuration_file(self, file_name: str) -> Dict[Any, Any]:
        return self.__load_configuration(file_name)

    def __load_configuration(self, file_name: str) -> Dict[Any, Any]:
        folder = self.environment.value
        with resources.open_text(folder, file_name) as f:
            return json.loads(f.read())
