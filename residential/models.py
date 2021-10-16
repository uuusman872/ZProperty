from django.db import models

# Create your models here.


class RedsidentialProperties(models.Model):
    Title = models.CharField(max_length=100)
    overview = models.TextField()
    Dashboard_Image = models.ImageField(upload_to="ResidentialInvesment", null=True)
    Price = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    num_bedRooms = models.CharField(max_length=100)
    num_WashRooms = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.Title)


class ResidentialPropertiesImage(models.Model):
    property = models.ForeignKey(RedsidentialProperties, models.CASCADE)
    description = models.TextField()
    Image = models.ImageField(upload_to="ResidentialInvesment/Gallery")

    def __str__(self) -> str:
        return str(self.property)
