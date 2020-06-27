from main.src.service.broker_service import *

bs = BrokerService(password='', username='', port=5672, queue='python_queue', host='', vhost='')
bs.send({
    "process": "predict",
    "environment": "DEVELOPMENT",
    "force": 'TRUE'
})
