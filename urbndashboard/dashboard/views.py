from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse
import requests

class Dashboard(View):

    def get(self, request):
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)

def play_count_by_month(request, brand, saleType, date):
    r = requests.get('http://misl-dev.urbanout.com/api/v1/sales/' + saleType + '/hours/' + brand + '/' + date)
    data = r.json()["details"];
    return JsonResponse(list(data), safe=False)