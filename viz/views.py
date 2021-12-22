from django.shortcuts import render
from . import get_data
from django.http import HttpResponse, JsonResponse
import json

def view_all(request):
	data = get_data.generate_geojson()
	print("Before dumps type: ", type(data))
	data = json.dumps(data)
	print("After dumps type: ", type(data))
	context = {"data":data}
	return render(request, "viz/index.html", context)

