from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def api_home(request, *args,**kwargs):
    body = request.body
    print(body)
    return JsonResponse({"message":"Hi there, this is shohan"})