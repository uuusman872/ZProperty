from django.contrib import admin
from .models import ResidentialPropertiesImage, RedsidentialProperties
# Register your models here.


class InlineResidentialImages(admin.TabularInline):
    model = ResidentialPropertiesImage


class InlineResidentialPro(admin.ModelAdmin):
    inlines = [InlineResidentialImages]


admin.site.register(RedsidentialProperties, InlineResidentialPro)