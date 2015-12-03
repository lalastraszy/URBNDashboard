from django.http import JsonResponse
import requests


def get_all_brands(request):
    r = requests.get('http://misl-dev.urbanout.com/api/v1/sales/brands')
    data = r.json()["details"]
    return JsonResponse(list(data), safe=False)

