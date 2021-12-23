from django.db import models
from django.http import request, response
from django.shortcuts import render  , HttpResponse
import razorpay  
import os , json
from home.models import suppotors


def application(environ, start_response):
  if environ['REQUEST_METHOD'] == 'OPTIONS':
    start_response(
      '200 OK',
      [
        ('Content-Type', 'application/json'),
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Headers', 'Authorization, Content-Type'),
        ('Access-Control-Allow-Methods', 'POST'),
      ]
    )
    return ''



# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')


def contact(request):
    return render(request,'contact.html')


def donate(request):
    return render(request,'donate.html')

def download(request):
    
    supoters = suppotors.objects.filter().order_by('amount')
  


    import requests
    from django.core.exceptions import ObjectDoesNotExist

    url = "https://api.razorpay.com/v1/payments/"

    payload = ""
    headers = {
    'Authorization': 'Basic cnpwX2xpdmVfY3h5UmY0eGltY2hKSWw6Tm9PMWVIOWc4dTMzSmUya2ZTU1FFUW5B'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data =response.text





    parsed = json.loads(data)


    items =parsed['items']
    
    for i in items:
   
        if i['status'] != "failed":
                ins = suppotors(name=i['notes']['name'] , amount = i['amount'])
                duplicatecheck(ins)
                if(duplicatecheck(ins)):
                    ins.save()
               
           

                
                
                
            # print(field_value)
            # if i['notes']['name'] != field_value:
            #     print(i['notes']['name'] , field_value)
            #     ins = suppotors(name=i['notes']['name'] , amount = i['amount'])
            #     ins.save()
            # else:
            #     print("error")
    


    return render(request,'download.html' , {'supoters': supoters})
# field_name = 'name'
# obj = suppotors.objects.first()
# field_object = suppotors._meta.get_field(field_name)
# field_value = field_object.value_from_object(obj)
# print(field_value)


# render(request,'download.html',{'supoters': supoters})

def duplicatecheck(ins):
    supoters = suppotors.objects.filter().order_by('amount')
    for t in supoters:
        if t.name==ins.name:
            print(t.name , ins.name)
            return False
            
    return True

