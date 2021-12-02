from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


# Create your models here.

class Question(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    posted_date = models.DateTimeField(auto_now=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Question = models.TextField(null=True)


class PropertyInquiry(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    posted_date = models.DateTimeField(auto_now=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Question = models.TextField(null=True)
    property_type = models.CharField(max_length=100, null=True, blank=True)
    property_name = models.CharField(max_length=100, null=True, blank=True)
