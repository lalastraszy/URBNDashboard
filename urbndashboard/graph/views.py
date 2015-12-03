from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class Graph(View):
	
	def get(self, request):
		params = dict()
		params['name'] = 'graph1'
		return render(request, 'graph.html', params)
