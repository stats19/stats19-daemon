import os
from dataclasses import dataclass

import logging

from main.src.services import  APIResponsesList
from settings import dotenv_path

logger = logging.getLogger(__name__)


@dataclass
class MainProcess:

    @classmethod
    def run(cls) -> None:
        logger.info("Main process")
        logger.info("api Responses: \n")
        for r in APIResponsesList:
            logger.info(r.__str__())



