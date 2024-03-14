from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from email_sender_app.models import EmailLogs
from email_sender_app.serializers import EmailLogsSerializer
from rest_framework.permissions import AllowAny
import pandas as pd
from django.core.mail import send_mail


class SendEmailAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        if request.FILES:
            file = request.FILES['file']
            df = pd.read_excel(file)
            for indx,row in df.iterrows():
                send_mail(row['subject'],row['body'],row['sender'],[row['receiver']])
                EmailLogs.objects.create(sender=row['sender'],receiver=row['receiver'],\
                                        subject=row['subject'],body=row['body']) 
            return Response({'msg':'Done'})
        else:
            serializer = EmailLogsSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            for data in serializer.data:
                send_mail(data['subject'],data['body'],data['sender'],[data['receiver']])
            serializer.save()           
            return Response(serializer.data,status=status.HTTP_200_OK)
        # return super().post(request, *args, **kwargs)