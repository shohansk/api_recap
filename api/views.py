from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse,HttpResponse
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer
from products.models import Product

@api_view(["GET"])
def api_home(request, *args,**kwargs):
    """
    DRF api view
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
       # data = model_to_dict(model_data, fields=['id','title','sale_pice'])

    return Response(data)