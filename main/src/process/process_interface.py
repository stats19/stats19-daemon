import logging
from abc import ABC
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class Process(ABC):
    use_asyncio: bool
    force_process_execution: Optional[bool]

    def call_process(self) -> None:
        pass
