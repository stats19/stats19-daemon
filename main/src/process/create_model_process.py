import logging
import random
from typing import List, Tuple

import matplotlib.pyplot as plt
from dataclasses import dataclass

import numpy as np
from tensorflow.keras.callbacks import TensorBoard
from sklearn.metrics import confusion_matrix

from main.src.exporter.broker_exporter import BrokerExporter
from main.src.importer.api_importer import ApiImporter
from main.src.importer.broker_importer import BrokerImporter
from main.src.model.api_model import FullMatch
from main.src.process.process_interface import Process
from main.src.service.dataset_service import DatasetService


logger = logging.getLogger(__name__)
logging.getLogger('matplotlib').setLevel(logging.ERROR)


@dataclass
class CreateModelProcess(Process):

    importer_broker: BrokerImporter
    importer_api: ApiImporter
    exporter_broker: BrokerExporter

    name: str

    def call_process(self) -> None:
        logger.info(f'Call process {self.name}')

        self.exporter_broker.send({
            "process": self.name,
            "status": 'RUNNING',
        })

        if self.force_process_execution:
            self._start_safe_process()
        else:
            self._start_safe_process()

        logger.info(f'End process {self.name}')

        self.exporter_broker.send({
            "process": self.name,
            "status": 'ENDED',
        })

    def _start_safe_process(self):
        logger.info('Working')

        matches = self.importer_api.get_all_matches()
        matches_test, matches_train = self._extract_match_value(matches)

        (x_train, y_train), (x_test, y_test) = DatasetService.load_dataset(matches_train, matches_test)
        print(x_train.shape)
        print(y_train.shape)
        print(x_test.shape)
        print(y_test.shape)

        # model = DatasetService.create_linear_model()
        model = DatasetService.create_mlp_model()

        true_values = np.argmax(y_train, axis=1)
        preds = np.argmax(model.predict(x_train), axis=1)

        print("Confusion Train Matrix Before Training")
        print(confusion_matrix(true_values, preds))

        true_values = np.argmax(y_test, axis=1)
        preds = np.argmax(model.predict(x_test), axis=1)
        print("Confusion Test Matrix Before Training")
        print(confusion_matrix(true_values, preds))

        print(f'Train Acc : {model.evaluate(x_train, y_train)[1]}')
        print(f'Test Acc : {model.evaluate(x_test, y_test)[1]}')

        print(confusion_matrix(true_values, preds))

        logs = model.fit(x_train, y_train, batch_size=64, epochs=DatasetService.epoch, verbose=1,
                         validation_data=(x_test, y_test), callbacks=[TensorBoard()])

        plt.plot(logs.history['accuracy'])
        plt.plot(logs.history['val_accuracy'])
        plt.show()

        plt.plot(logs.history['loss'])
        plt.plot(logs.history['val_loss'])
        plt.show()

        model.save('linear_model.keras')

    @staticmethod
    def _extract_match_value(matches: List[FullMatch]) -> Tuple[List[FullMatch], List[FullMatch]]:
        pourcentage = int(len(matches) * 0.2)
        random.shuffle(matches)

        return matches[0:pourcentage], matches[pourcentage::]




