from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse
import requests


class Graph(View):

    def get(self, request):
        params = dict()
        params['name'] = 'graph1'
        return render(request, 'graph.html', params)


def get_graph_data(request, brand, type, statType, date):
    r = requests.get('http://misl-dev.urbanout.com/api/v1/sales/' + type + '/' + statType + '/' + brand + '/' + date)
    data = r.json()["details"];
    return JsonResponse(list(data), safe=False)