from django.http import HttpResponse
from django.http import HttpResponse
import requests
from django.shortcuts import render
import uuid
reference_id = uuid.uuid4()

def login(request):

    url = "https://test.cashfree.com/api/v1/order/create"

    payload = {
        "appid": "TEST3931154d6e90b54bfbc3b4946d511393",
        "secretKey": "TEST701a10a8d7389d719903c77dda9fa993fbc0db63",
        "orderId": reference_id,
        "orderAmount": "1",
        "orderCurrency": "INR",
        "oderNote": "pay",
        "customerName": "mohan",
        "customerEmail": "abcd@gmail.com",
        "customerPhone": "8494863493",
        # "returnUrl": "https://cashfree.com",

         "notifyUrl": "https://channi.vercel.app/payment_info",
    }


    response = requests.request("POST", url, data=payload)
    print(response.text)

    return render(request,'home.html',{"response":response.text})


def payment_info(request):
    print("ggg")
    return render(request,'login.html')

