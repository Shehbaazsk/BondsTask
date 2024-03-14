from rest_framework import serializers
from .models import EmailLogs

class EmailLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLogs
        fields = '__all__'
