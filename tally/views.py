import os
import requests


from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    binUrl = 'http://httpbin.org/get'
    url = os.getenv('BLIZZARD_WEB_API_URL') + '/wow/guild/Thunderhorn/Fallen Empire'
    url_params = {
        'fields': 'members',
        'locale': 'en_US',
        'apikey': os.getenv('BLIZZARD_WEB_API_PUBLIC_KEY')
    }
    r = requests.get(url, params=url_params)
    return HttpResponse(r.text)

