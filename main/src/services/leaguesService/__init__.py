import requests
from main.src.services.apiUtils import RequestResponse, API_ENDPOINT


leagues_endpoint = API_ENDPOINT +"/api/leagues"
# Get
Data = requests.get(leagues_endpoint).text
Leagues_response = RequestResponse("GET", leagues_endpoint, Data)