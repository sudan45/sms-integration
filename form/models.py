from django.db import models

# Create your models here.


class Message(models.Model):
    to = models.CharField(max_length=1000)
    message = models.CharField(max_length=5000, null=False)



