import os
from urllib.parse import urlparse, urlencode
import requests


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def login(request):
    url = os.getenv('BLIZZARD_WEB_API_AUTHORIZE_URI')
    url_params = {
        'redirect_uri': 'http://localhost',
        'client_id': os.getenv('BLIZZARD_WEB_API_PUBLIC_KEY'),
        'scope': 'wow.profile',
        'response_type': 'code',
        'state': 'sodfmadasdgas'
    }
    url += '?' + urlencode(url_params)
    #r = requests.get(url, params=url_params)
    return HttpResponseRedirect(url)
