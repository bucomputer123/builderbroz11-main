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
    return render(request,'download.html')


# import requests

# url = "https://api.razorpay.com/v1/payments/"

# payload = ""
# headers = {
#   'Authorization': 'Basic cnpwX2xpdmVfY3h5UmY0eGltY2hKSWw6Tm9PMWVIOWc4dTMzSmUya2ZTU1FFUW5B'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# data =response.text





# parsed = json.loads(data)


# items =parsed['items']

# for i in items:
#    if i['status'] != "failed":
#       print(i['amount'])
#       ins = suppotors(name=i['notes']['name'] , amount = i['amount'])
#       ins.save()
  
#print(resp)





# url = "https://api.twitter.com/2/users/1471330955637837826/tweets"

# payload={}
# headers = {
#   'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAF%2BpXAEAAAAA%2F%2BdZ5p4EyPY5vUBRNYNwcfP7WcA%3DmGYtD5dumYaoOD4K1eM7San4B3GCJ5gg6CANz6YflrQAN1k4tZ',
#   'Cookie': 'guest_id=v1%3A163982968721781484; guest_id_ads=v1%3A163982968721781484; guest_id_marketing=v1%3A163982968721781484; personalization_id="v1_BYscqoAV+ygfTMR4hLC+Cw=="'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
# responses = {
    # "entity":"collection",
    # "count":4,
    # "items":[{
    #     "id":"pay_IYrfEU5O6dEu5R",  
    #     "entity":"payment",
    #     "amount":200,
    #     "currency":"INR",
    #     "status":"failed",
    #     "order_id":"order_IYrf1ZE5MhCYE4",
    #     "invoice_id":null,
    #     "international":false,
    #     "method":"upi",
    #     "amount_refunded":0,
    #     "refund_status":null,
    #     "captured":false,
    #     "description":null,
    #     "card_id":null,
    #     "bank":null,
    #     "wallet":null,
    #     "vpa":null,
    #     "email":"bigppsixtynine@gmail.com",
    #     "contact":"+919827688768",
    #     "notes":{"name":"jj",
    #     "email":"bigppsixtynine@gmail.com","phone":"9827688768"},"fee":null,"tax":null,"error_code":"BAD_REQUEST_ERROR","error_description":"You may have cancelled the payment or there was a delay in response from the UPI app.","error_source":"customer","error_step":"payment_authentication","error_reason":"payment_cancelled","acquirer_data":{"rrn":null},"created_at":1639814509},{"id":"pay_IYrLItk4UtEaQa","entity":"payment","amount":100,"currency":"INR","status":"captured","order_id":"order_IYrL5vpS0Yz3sf","invoice_id":null,"international":false,"method":"upi","amount_refunded":0,"refund_status":null,"captured":true,"description":null,"card_id":null,"bank":null,"wallet":null,"vpa":"8109204371@ybl","email":"bigppsixtynine@gmail.com","contact":"+919827688768","notes":{"name":"rajvendra","email":"bigppsixtynine@gmail.com","phone":"9827688768"},"fee":2,"tax":0,"error_code":null,"error_description":null,"error_source":null,"error_step":null,"error_reason":null,"acquirer_data":{"rrn":"135242308615"},"created_at":1639813377},{"id":"pay_IUu4zxWHm7YLzg","entity":"payment","amount":800,"currency":"INR","status":"failed","order_id":"order_IUu4u1DRVN6cIz","invoice_id":null,"international":false,"method":"upi","amount_refunded":0,"refund_status":null,"captured":false,"description":null,"card_id":null,"bank":null,"wallet":null,"vpa":null,"email":"builderbrosinc706@gmail.com","contact":"+918109204371","notes":{"email":"builderbrosinc706@gmail.com","phone":"08109204371"},"fee":null,"tax":null,"error_code":"BAD_REQUEST_ERROR","error_description":"You may have cancelled the payment or there was a delay in response from the UPI app.","error_source":"customer","error_step":"payment_authentication","error_reason":"payment_cancelled","acquirer_data":{"rrn":null},"created_at":1638949656},{"id":"pay_IUt4YifdYKMChN","entity":"payment","amount":100,"currency":"INR","status":"captured","order_id":"order_IUt4PSrCju31f3","invoice_id":null,"international":false,"method":"upi","amount_refunded":0,"refund_status":null,"captured":true,"description":null,"card_id":null,"bank":null,"wallet":null,"vpa":"8109204371@ybl","email":"builderbrosinc706@gmail.com","contact":"+918109204371","notes":{"email":"builderbrosinc706@gmail.com","phone":"8109204371","name":"raj","address":"shivcity","city":"bhopal","pincode":"462022","state":"mp"},"fee":2,"tax":0,"error_code":null,"error_description":null,"error_source":null,"error_step":null,"error_reason":null,"acquirer_data":{"rrn":"134240567657"},"created_at":1638946109}]}



# data = open('static/response_.json' , 'r')
# name = response_json['items']
# amount = 
# json_files = [pos_json for pos_json in os.listdir(data_loc) if pos_json.endswith('.json')]
# response_file = json.load(data)
# ins = suppotors(response_file.items)
# items =response_file['items']
 

# if i :
#   for i in items:
#     if i['status'] != "failed":
#       print(i['notes']['name'])
      # ins = suppotors(name=i['notes']['name'] , amount = i['amount'])
      # ins.save()
  


