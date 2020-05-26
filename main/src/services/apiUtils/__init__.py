from settings import Host, Port

API_ENDPOINT = "http://" + Host + ":" + Port

class RequestResponse:

    def __init__(self, method, url, response):
        self.method = method
        self.url = url
        self.response = response

    def _response(self):
        return {'method': self.method, 'url': self.url, 'data': self.response}

    def __str__(self):
        return self._response()