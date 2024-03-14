import datetime
from .models import EmailLogs
from django.db.models import Count

def count_of_email(minutes=60):
    current_time = datetime.datetime.now()
    calculate_time = current_time - datetime.timedelta(minutes=minutes)
    email_count = EmailLogs.objects.filter(timestamp__range=(calculate_time,current_time))\
                                    .values('sender','receiver').annotate(count_mail=Count('id'))
    for data in email_count:
        print(data)