from django.views.generic import View
from django.shortcuts import render


class Dashboard(View):

    def get(self, request):
        params = dict()
        params['name'] = 'Django'
        return render(request, 'base.html', params)