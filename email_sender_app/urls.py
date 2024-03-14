from django.urls import path
from .views import send_email_api

app_name = 'email_sender_app'

urlpatterns = [
    path('send_email/', send_email_api, name='send_email')
]
