

from main.src.service.broker_service import *

bs = BrokerService(password='runner', username='runner', port=5672, queue='runner2', host='127.0.0.1')
bs.send({"process": "predict"})