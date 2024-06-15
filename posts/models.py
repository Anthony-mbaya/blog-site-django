from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model): #First database table
    title = models.CharField(max_length=255) #few xters
    body = models.CharField(max_length=10000000) #body contains a lot of characters
    date_created = models.DateTimeField(default=datetime.now, blank=True) #get current date
