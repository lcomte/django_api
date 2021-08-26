import json

import requests
from django.http.response import JsonResponse
from django.core.validators import URLValidator
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Create your views here.
@api_view(['GET'])
def eurovalue(request):
    response_btc = requests.request("GET", "https://blockchain.info/ticker")
    json_result = response_btc.json()
    headers = {
        'Accept': 'application/vnd.sdmx.data+json;version=1.0.0-wd'
    }
    response_gbp = requests.request("GET", "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.GBP.EUR.SP00.A?updatedAfter=2021-07-01", headers=headers)
    json_resp = response_gbp.json()
    value_btc_eur = json_result["EUR"]["15m"]
    value_gbp = json_resp['dataSets'][0]["series"]["0:0:0:0:0"]["observations"]["0"][0]
    return JsonResponse({'bitcoin_eur': json_result["EUR"]["15m"], 'eur_to_gbp': json_resp['dataSets'][0]["series"]["0:0:0:0:0"]["observations"]["0"][0], "bitcoin_gbp": value_btc_eur * value_gbp}, status=status.HTTP_200_OK)

@api_view(['POST'])
def webpageData(request):
    loader = json.loads(request.body)
    url = loader["url"]
    try:
        validator = URLValidator()
        validator(url)
    except:
        return JsonResponse({'message': 'URL Is not correct'}, status=status.HTTP_400_BAD_REQUEST)
    parsedUrl = urlparse(url)
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text, 'html.parser')
    photos = []
    for photo in soup.find_all('img'):
        photos.append(photo.get('src'))
    stylesheets_counter = len(soup.find_all('style'))
    return JsonResponse({'domain_name': parsedUrl.netloc, 'protocol': parsedUrl.scheme, 'title': soup.title.get_text(), 'image': photos, 'stylesheets': stylesheets_counter}, status=status.HTTP_200_OK)
