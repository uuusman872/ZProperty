from django.contrib import admin
from .models import ResidentialPropertiesImage, ResidentialProperties, Amenitie, PaymentPlans, InvestmentPlans


# Register your models here.


class InlineResidentialImages(admin.TabularInline):
    model = ResidentialPropertiesImage


class InlineAmenitie(admin.TabularInline):
    model = Amenitie


class PaymentPlanInline(admin.TabularInline):
    model = PaymentPlans


class InvesmentPlanInline(admin.TabularInline):
    model = InvestmentPlans


class InlineResidentialPro(admin.ModelAdmin):
    inlines = [InlineResidentialImages, InlineAmenitie, PaymentPlanInline, InvesmentPlanInline]


admin.site.register(ResidentialProperties, InlineResidentialPro)
