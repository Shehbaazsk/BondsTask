from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import EmailLogs
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

# Create your views here.

@csrf_exempt
def send_email_api(request):
    if request.method == 'POST':
        if request.FILES:
            file = request.FILES['file']
            df = pd.read_excel(file)
            for indx,row in df.iterrows():
                print(row['sender'])
                send_mail(row['subject'],row['body'],row['sender'],[row['receiver']])
                EmailLogs.objects.create(sender=row['sender'],receiver=row['receiver'],\
                                        subject=row['subject'],body=row['body'])   
        else:
            subject = request.POST['subject']
            body = request.POST['body']
            sender = request.POST['sender']
            receiver = request.POST['receiver']
            send_mail(subject,body,sender,[receiver])
            EmailLogs.objects.create(sender=sender,receiver=receiver,subject=subject,body=body)                 
        return JsonResponse({"msg":"Email Sent"})