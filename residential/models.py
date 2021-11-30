import datetime

from django.db import models


# Create your models here.


class ResidentialProperties(models.Model):
    Title = models.CharField(max_length=100)
    overview = models.TextField()
    Dashboard_Image = models.ImageField(upload_to="ResidentialInvesment", null=True)
    flowPlan_Image = models.ImageField(upload_to="ResidentialInvesment/flowPlan", null=True)
    Price = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    locationFrame = models.TextField(null=True, blank=True)
    num_bedRooms = models.CharField(max_length=100)
    num_WashRooms = models.CharField(max_length=100)
    num_Garage = models.CharField(max_length=100, null=True)
    video_url = models.TextField(null=True)
    property_type = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    uploaded_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.Title)


class ResidentialPropertiesImage(models.Model):
    property = models.ForeignKey(ResidentialProperties, models.CASCADE)
    description = models.TextField(null=True, blank=True)
    Image = models.ImageField(upload_to="ResidentialInvesment/Gallery")

    def __str__(self) -> str:
        return str(self.property)


class Amenitie(models.Model):
    property = models.ForeignKey(ResidentialProperties, models.CASCADE)
    name = models.CharField(max_length=100)


class PaymentPlans(models.Model):
    plan = models.ForeignKey(ResidentialProperties, on_delete=models.CASCADE)
    Instalment_name = models.CharField(max_length=100, null=True)
    Installment_plan = models.TextField(null=True)

    def __str__(self):
        return str(self.plan)


class InvestmentPlans(models.Model):
    plan = models.ForeignKey(ResidentialProperties, on_delete=models.CASCADE)
    investmentPlan = models.CharField(max_length=100, null=True, blank=True)
    investmentDetails = models.TextField(null=True, blank=True)
