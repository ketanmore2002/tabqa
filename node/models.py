from django.db import models
import uuid 

# Create your models here.


class dataset(models.Model):
    name = models.CharField(max_length=300,blank=True,null=True)
    description = models.CharField(max_length=300,blank=True,null=True)
    data =  models.TextField(blank=True,null=True)
    uuid = models.UUIDField(default = uuid.uuid4, editable = True)
    time = models.TimeField(auto_now=True,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    user_name = models.CharField(max_length=300,blank=True,null=True)
    user_id = models.CharField(max_length=300,blank=True,null=True)


class logs(models.Model):
    data_uuid =  models.CharField(max_length=300,blank=True,null=True)
    query =  models.CharField(max_length=300,blank=True,null=True)
    answer =  models.CharField(max_length=300,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    user_name = models.CharField(max_length=300,blank=True,null=True)
    # user_id = models.CharField(max_length=300,blank=True,null=True)
    response_time = models.CharField(max_length=300,blank=True,null=True)