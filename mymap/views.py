from django.shortcuts import render
import urllib
import urllib.request
import json
from pprint import pprint

def mymap(request):

    url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat=37.467116&lng=126.815328&m=100000"
    re = urllib.request.Request(url, headers={'User-Agent': 's'})
    response = urllib.request.urlopen(re)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()

        dict = json.loads(response_body.decode('utf-8'))

        a = (dict['count'])
        return render(request, 'mymap/index.html',{'dict':dict['stores'],'num':a})
    else:
        return render(request, 'mymap/index.html')