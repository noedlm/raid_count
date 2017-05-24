import os
import pdb
import requests
from urllib.parse import urlparse, urlencode


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def login(request):
    url = os.getenv('BLIZZARD_WEB_API_AUTHORIZE_URI')
    url_params = {
        'redirect_uri': 'https://raid-count.herokuapp.com/auth/consume',
        'client_id': os.getenv('BLIZZARD_WEB_API_PUBLIC_KEY'),
        'scope': 'wow.profile',
        'response_type': 'code',
    }
    url += '?' + urlencode(url_params)
    #r = requests.get(url, params=url_params)

    return HttpResponseRedirect(url)


def consume(request):
    if 'code' in request.GET:
        code = request.GET['code']
        url = os.getenv('BLIZZARD_WEB_API_TOKEN_URI')
        payload = {
            'client_id': os.getenv('BLIZZARD_WEB_API_PUBLIC_KEY'),
            'client_secret': os.getenv('BLIZZARD_WEB_API_PRIVATE_KEY'),
            'code': code,
            'grant_type': 'authorization_code',
            'scope': 'wow.profile',
            'redirect_uri': 'https://raid-count.herokuapp.com/auth/consume',
        }
        r = requests.post(url, payload)

        return HttpResponse(r)

    return 'could not get that damn token!'
