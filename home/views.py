from django.http import response
from django.shortcuts import render  , HttpResponse
import razorpay  

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


   
client = razorpay.Client(auth=("rzp_live_cxyRf4ximchJIl", "NoO1eH9g8u33Je2kfSSQEQnA"))
resp = client.payment.fetch_all()
print(resp)









import requests

url = "https://api.twitter.com/2/users/1471330955637837826/tweets"

payload={}
headers = {
  'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAF%2BpXAEAAAAA%2F%2BdZ5p4EyPY5vUBRNYNwcfP7WcA%3DmGYtD5dumYaoOD4K1eM7San4B3GCJ5gg6CANz6YflrQAN1k4tZ',
  'Cookie': 'guest_id=v1%3A163982968721781484; guest_id_ads=v1%3A163982968721781484; guest_id_marketing=v1%3A163982968721781484; personalization_id="v1_BYscqoAV+ygfTMR4hLC+Cw=="'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


