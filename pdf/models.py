from django.db import models
import os
from twilio.rest import Client
# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    skill = models.TextField(max_length=1000)
    about_you = models.TextField(max_length=1000)
    previous_work = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        account_sid = 'AC2702048643a5c57091083726a532fe13'
        auth_token = 'fd1867a9a95391973257248d13e9d203'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                     body=f"{self.name} with {self.phone} just submitted in resume",
                     from_='+16626671874',
                     to='+2348033248599'
                 )

        print(message.sid)
        return super().save(*args, **kwargs)
