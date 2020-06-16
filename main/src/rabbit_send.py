

from main.src.service.broker_service import *

bs = BrokerService(password='runner', username='runner', port=5672, queue='python_queue', host='127.0.0.1')
bs.send({
    "process": "predict",
    "environment": "DEVELOPMENT",
    "force": 'TRUE'
})
