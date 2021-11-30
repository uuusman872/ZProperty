import datetime

from django.db import models


# Create your models here.


class OFFPlanAndInvestment(models.Model):
    Title = models.CharField(max_length=200)
    overview = models.TextField()
    Location = models.CharField(max_length=200)
    locationFrame = models.TextField(null=True, blank=True)
    Price = models.CharField(max_length=100)
    video_url = models.TextField(null=True)
    Completion_date = models.DateField()
    flowPlan_Image = models.ImageField("OfPlanInvesments/flowPlan", null=True, blank=True)
    Dashboard_Image = models.ImageField(upload_to="OfPlanInvesments/")
    Developer = models.CharField(max_length=200, null=True)
    Development_type = models.TextField(null=True)
    num_bedRooms = models.CharField(max_length=100, null=True)
    num_WashRooms = models.CharField(max_length=100, null=True, default="1")
    num_Garage = models.CharField(max_length=100, null=True, default="1")
    Area = models.CharField(max_length=100, null=True, default="1")
    uploaded_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.Title)


class OffPlanGallery(models.Model):
    plan = models.ForeignKey(OFFPlanAndInvestment, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to="OfPlanInvesments/Gallery", null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.plan)


class Amenitie(models.Model):
    property = models.ForeignKey(OFFPlanAndInvestment, models.CASCADE)
    name = models.CharField(max_length=100)


class PaymentPlans(models.Model):
    plan = models.ForeignKey(OFFPlanAndInvestment, on_delete=models.CASCADE)
    Instalment_name = models.CharField(max_length=100, null=True)
    Installment_plan = models.TextField(null=True)

    def __str__(self):
        return str(self.plan)


class InvestmentPlans(models.Model):
    plan = models.ForeignKey(OFFPlanAndInvestment, on_delete=models.CASCADE)
    investmentPlan = models.CharField(max_length=100, null=True, blank=True)
    investmentDetails = models.TextField(null=True, blank=True)
