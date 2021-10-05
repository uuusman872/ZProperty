from django.db import models

# Create your models here.

class OfPlaneInvesments(models.Model):
    planeName = models.CharField(max_length=200)
    overview = models.TextField()
    location = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    complition_date = models.DateField()
    dahboard_images = models.ImageField(upload_to="Media/OfPlanInvesments/")

    def __str__(self):
        return self.planeName

class OffPlanGallery(models.Model):
    plan = models.ForeignKey(OfPlaneInvesments, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Media/OfPlanInvesments/Gallery")
    def __str__(self):
        return self.plan