from typing import List

import numpy as np
from dataclasses import dataclass, field
from enum import Enum
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.activations import sigmoid, tanh

from main.src.model.api_model import FullMatch


class WHOWON(Enum):
    HOMEWON = [1, 0, 0]
    AWAYWON = [0, 1, 0]
    EQUALITY = [0, 0, 1]


@dataclass
class DatasetService(object):

    epoch: int = field(default=50)

    @staticmethod
    def load_dataset(matches : List[FullMatch], matches_test: List[FullMatch]):
        Ximgs = []
        y_train = []
        # For match in matches
        # Ximgs.append() data
        # y_train.append() gagnant du match [1,0] ou [0,1]


        # boucle reponse json
        # ajoute match [equipe home , equipe away]
        # if( json.homescore > json.awaysore)
        #   WHOWON.HOMEWON.value
        # elif ( json.homescore < json.awaysore)
        #   WHOWON.AWAYWON.value
        # else
        #   WHOWON.EQUALITY.value

        for match in matches:
            Ximgs.append(np.array([match.team_home_id, match.team_away_id]))
            if match.goal_away > match.goal_home:
                y_train.append(WHOWON.AWAYWON.value)
            elif match.goal_away < match.goal_home:
                y_train.append(WHOWON.HOMEWON.value)
            else:
                y_train.append(WHOWON.EQUALITY.value)

        Ximgs_test = []
        y_test = []

        for match in matches_test:
            Ximgs_test.append(np.array([match.team_home_id, match.team_away_id]))
            if match.goal_away > match.goal_home:
                y_test.append(WHOWON.AWAYWON.value)
            elif match.goal_away < match.goal_home:
                y_test.append(WHOWON.HOMEWON.value)
            else:
                y_test.append(WHOWON.EQUALITY.value)

        # For match in matches
        # Ximgs.append() data
        # y_train.append() gagnant du match [1,0] ou [0,1]

        x_train = np.array(Ximgs)
        y_train = np.array(y_train)
        x_test = np.array(Ximgs_test)
        y_test = np.array(y_test)

        return (x_train, y_train), (x_test, y_test)

    @staticmethod
    def create_linear_model():
        model = Sequential()
        model.add(Flatten())
        model.add(Dense(3, activation=sigmoid))
        model.compile(optimizer=SGD(), loss=mean_squared_error, metrics=['accuracy'])
        return model

    @staticmethod
    def create_mlp_model():
        model = Sequential()
        model.add(Flatten())
        model.add(Dense(256, activation=tanh))
        model.add(Dense(256, activation=tanh))
        model.add(Dense(3, activation=sigmoid))
        model.compile(optimizer=SGD(), loss=mean_squared_error, metrics=['accuracy'])
        return model