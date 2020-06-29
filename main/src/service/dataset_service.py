from dataclasses import dataclass, field
from enum import Enum
from typing import List

import numpy as np
from tensorflow.keras.activations import sigmoid, tanh
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.utils.np_utils import to_categorical

from main.resources.dev.data.data import teams
from main.src.model.api_model import FullMatch


class WHOWON(Enum):
    HOMEWON = [1, 0, 0]
    EQUALITY = [0, 1, 0]
    AWAYWON = [0, 0, 1]


@dataclass
class DatasetService(object):
    epoch: int = field(default=101)

    @staticmethod
    def load_dataset(matches: List[FullMatch], matches_test: List[FullMatch]):
        Ximgs = []
        y_train = []

        for match in matches:
            Ximgs.append(np.array([match.home.team_id, match.away.team_id]))
            if match.away.goals > match.home.goals:
                y_train.append(WHOWON.AWAYWON.value)
            elif match.away.goals < match.home.goals:
                y_train.append(WHOWON.HOMEWON.value)
            else:
                y_train.append(WHOWON.EQUALITY.value)

        Ximgs_test = []
        y_test = []

        for match in matches_test:
            Ximgs_test.append(np.array([match.home.team_id, match.away.team_id]))
            if match.away.goals > match.home.goals:
                y_test.append(WHOWON.AWAYWON.value)
            elif match.away.goals < match.home.goals:
                y_test.append(WHOWON.HOMEWON.value)
            else:
                y_test.append(WHOWON.EQUALITY.value)

        x_train = to_categorical(Ximgs)
        y_train = np.array(y_train)
        x_test = to_categorical(Ximgs_test)
        y_test = np.array(y_test)

        return (x_train, y_train), (x_test, y_test)

    @staticmethod
    def create_linear_model():
        model = Sequential()
        model.add(Flatten())
        model.add(Dense(3, activation=tanh))
        model.compile(optimizer=SGD(), loss=mean_squared_error, metrics=['accuracy'])
        return model

    @staticmethod
    def create_mlp_model():
        model = Sequential()
        model.add(Flatten())
        model.add(Dense(np.argmax(teams), activation=tanh))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(np.argmax(teams), activation=tanh))
        model.add(Dense(3, activation=sigmoid))
        model.compile(optimizer='rmsprop', loss=mean_squared_error, metrics=['accuracy'])
        return model

    @staticmethod
    def predict_result_with_linear_model(matches: List[FullMatch]):
        model = load_model(f'./models/linear_model.keras')
        y = []

        for match in matches:
            y.append(np.array([match.home.team_id, match.away.team_id]))
        res = model.predict_classes(to_categorical(y))

        return res
