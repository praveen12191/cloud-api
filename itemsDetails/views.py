from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializer import ItemSerializer
api_view(['POST'])
@csrf_exempt
def details(request):
    name = request.POST['name']
    price = request.POST['price']
    img = request.POST['img']
    obj = Items.objects.create(name=name,price=price,img=img)
    obj.save()
    return JsonResponse([name,price,img],safe=False)

api_view(['GET'])
def getDetails(request):
    k = Items.objects.all()
    val = []
    for i in k:
        val.append({"name":i.name,"price":i.price,"img":i.img,"id":i.id})
    return JsonResponse(val,safe=False)

api_view(['POST'])
@csrf_exempt
def userDetails(request):
    username = request.POST['username']
    phonenumber = request.POST['phonenumber']
    password = request.POST['password']
    address = request.POST['address']
    print(username,address)
    user = User.objects.crete(username=username,phonenumber=phonenumber,password=password,address=address)
    user.save()