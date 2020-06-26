import logging
from dataclasses import dataclass

from main.src.process.process_interface import Process

logger = logging.getLogger(__name__)


@dataclass
class MainProcess(Process):
    name: str

    def call_process(self) -> None:
        logger.info(f'Call process {self.name}')
