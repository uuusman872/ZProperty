from django.db import models


# Create your models here.


class OFFPlanAndInvestment(models.Model):
    PlanName = models.CharField(max_length=200)
    Overview = models.TextField()
    Location = models.CharField(max_length=200)
    Price = models.CharField(max_length=100)
    Completion_date = models.DateField()
    Dashboard_Image = models.ImageField(upload_to="OfPlanInvesments/")
    Developer = models.CharField(max_length=200, null=True)
    Development_type = models.TextField(null=True)

    def __str__(self):
        return str(self.PlanName)


class OffPlanGallery(models.Model):
    plan = models.ForeignKey(OFFPlanAndInvestment, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to="OfPlanInvesments/Gallery")

    def __str__(self):
        return str(self.plan)


class PaymentPlans(models.Model):
    plan = models.ForeignKey(OFFPlanAndInvestment, on_delete=models.CASCADE)
    Instalment_name = models.CharField(max_length=100, null=True)
    Installment_date = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.plan)