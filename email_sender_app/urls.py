from django.urls import path
from .views import send_email_api
from email_sender_app.api.api_views import SendEmailAPIView

app_name = 'email_sender_app'

urlpatterns = [
    path('send_email/', send_email_api, name='send_email'),
    path('send_email_api/',SendEmailAPIView.as_view())
]
