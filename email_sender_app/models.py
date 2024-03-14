from django.db import models

# Create your models here.

class EmailLogs(models.Model):
    sender = models.EmailField()
    receiver = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.receiver}'
    