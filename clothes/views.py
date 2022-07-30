from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required


# Create your views here.

from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt


def getAccessToken(request):
    consumer_key = 'TpCIJnUaLQLs1XLhMySKCEfgtPSWkZNU'
    consumer_secret = '1booBmyCQ3NHxT3Y'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request, id):
    orders = Client.objects.filter(paid=False)
    order = get_object_or_404(Client, id=id)


        # remove "+" from customer's phone number
    # for order in orders:  
    if order.paid == False:  
        mobile = order.phone_number
        phone = str(order.phone_number).translate({ord('+'): None})


        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": order.service.price,
            "PartyA": int(phone),  # replace with your phone number to get stk push...convert phone number to integer
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": int(phone),  # replace with your phone number to get stk push...convert phone number to integer
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Laundy",
            "TransactionDesc": "Testing stk push"
        }
        response = requests.post(api_url, json=request, headers=headers)
        # order = Client.objects.get(phone_number=mobile)
        order.paid=True
        order.payment_method = 'MPESA'
        order.save()

        return redirect('home')
    return HttpResponse('Already paid')    


# from django.http import HttpResponse, JsonResponse
# import requests
# from requests.auth import HTTPBasicAuth
# import json
# from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
# from django.views.decorators.csrf import csrf_exempt
# from .models import MpesaPayment


# def lipa_na_mpesa_online(request):
#     access_token = MpesaAccessToken.validated_mpesa_access_token
#     api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#     headers = {"Authorization": "Bearer %s" % access_token}
#     request = {
#         "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
#         "Password": LipanaMpesaPpassword.decode_password,
#         "Timestamp": LipanaMpesaPpassword.lipa_time,
#         "TransactionType": "CustomerPayBillOnline",
#         "Amount": 1,
#         "PartyA": 254728851119,  # replace with your phone number to get stk push
#         "PartyB": LipanaMpesaPpassword.Business_short_code,
#         "PhoneNumber": 254728851119,  # replace with your phone number to get stk push
#         "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
#         "AccountReference": "Henry",
#         "TransactionDesc": "Testing stk push"
#     }
#     response = requests.post(api_url, json=request, headers=headers)
#     return HttpResponse('success')
# @csrf_exempt
# def register_urls(request):
#     access_token = MpesaAccessToken.validated_mpesa_access_token
#     api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
#     headers = {"Authorization": "Bearer %s" % access_token}
#     options = {"ShortCode": LipanaMpesaPpassword.Business_short_code,
#                "ResponseType": "Completed",
#                "ConfirmationURL": "https://1def-102-222-144-66.in.ngrok.io//payment/confirmation",
#                "ValidationURL": "https://1def-102-222-144-66.in.ngrok.io//payment/validation"}
#     response = requests.post(api_url, json=options, headers=headers)
#     return HttpResponse(response.text)
# @csrf_exempt
# def call_back(request):
#     pass
# @csrf_exempt
# def validation(request):
#     context = {
#         "ResultCode": 0,
#         "ResultDesc": "Accepted"
#     }
#     return JsonResponse(dict(context))
# @csrf_exempt
# def confirmation(request):
#     mpesa_body =request.body.decode('utf-8')
#     mpesa_payment = json.loads(mpesa_body)
#     payment = MpesaPayment(
#         first_name=mpesa_payment['FirstName'],
#         last_name=mpesa_payment['LastName'],
#         middle_name=mpesa_payment['MiddleName'],
#         description=mpesa_payment['TransID'],
#         phone_number=mpesa_payment['MSISDN'],
#         amount=mpesa_payment['TransAmount'],
#         reference=mpesa_payment['BillRefNumber'],
#         organization_balance=mpesa_payment['OrgAccountBalance'],
#         type=mpesa_payment['TransactionType'],
#     )
#     payment.save()
#     context = {
#         "ResultCode": 0,
#         "ResultDesc": "Accepted"
#     }
#     return JsonResponse(dict(context))
@login_required
def home(request):

    clients_list = Client.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(clients_list, 10)

    try:
        clothes = paginator.page(page)
    except PageNotAnInteger:
        clothes = paginator.page(1)
    except EmptyPage:
        clothes = paginator.page(paginator.num_pages)



    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    sform = ServiceForm()
    if request.method == 'POST':
        sform = ServiceForm(request.POST)
        if sform.is_valid():
            sform.save()
            return redirect('home')  

    context = {
        'form':form,
        'clothes':clothes,
        'sform':sform


    }  
    return render(request, 'home.html', context)      

def clients(request):
    # clothes = Client.objects.all().order_by('-id')
    clients_list = Client.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(clients_list, 10)

    try:
        clothes = paginator.page(page)
    except PageNotAnInteger:
        clothes = paginator.page(1)
    except EmptyPage:
        clothes = paginator.page(paginator.num_pages)

    context = {
        'clothes':clothes
    }
    return render(request, 'clienst.html', context)      

def editClient(request, id):
    client = get_object_or_404(Client, id=id)

    form = ClientUpdateForm(instance=client)
    if request.method == 'POST':
        form = ClientUpdateForm(request.POST,instance=client)
        if form.is_valid():
            checkout = form.save(commit=False)
            checkout.served_by = request.user
            checkout.save()
            return redirect('home')

    context = {
        'form':form,
        'client':client

    }       

    return render(request, 'update.html', context)    

def editServicec(request, id):
    service = get_object_or_404(Service, id=id)

    form = ServiceForm(instance=client)
    if request.method == 'POST':
        form = ServiceForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form':form,
        'service':service

    }       

    return render(request, 'update.html', context)         

def clientDelete(request, id):
    client = get_object_or_404(Client, id=id)
    client.delete()
    return redirect('home')

def serviceDelete(request, id):
    service = get_object_or_404(Service, id=id)
    service.delete()
    return redirect('home')

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from datetime import datetime

def receipt(request, id):
    # Create a file-like buffer to receive PDF data.
    client = get_object_or_404(Client, id=id)

    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    # canvas.rect(x, y, width, height, stroke=1, fill=0)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(200,805, "LAUNDRY SERVICES RECEIPT")
    p.drawString(20,785, f"Receipt No: {client.order_no}")

    p.drawString(25,765, f"PAYMENT MODE")
    p.drawString(200,765, f"AMOUNT")
    p.drawString(300,765, f"SERVICE")
    p.drawString(400,765, f"DATE")
    p.line(10,760,580,760)


    p.drawString(25,740, f"{client.payment_method}")
    p.drawString(200,740, f"{client.service.price}")
    p.drawString(300,740, f"{client.service.service_name}")
    p.drawString(400,740, f"{client.check_out_date.strftime('%Y-%m-%d')}")
    p.drawString(20,660, f"served by:{client.served_by.username}")


    # date_time = now.



    # Close the PDF object cleanly, and we're done.
    # p.showPage()

    # p.setPageSize((500, 300))
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='laundryReceipt.pdf')                
    