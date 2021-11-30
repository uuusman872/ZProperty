from django.contrib import admin
from .models import OFFPlanAndInvestment, OffPlanGallery, PaymentPlans, Amenitie, InvestmentPlans


# Register your models here.


class GalleryInline(admin.TabularInline):
    model = OffPlanGallery


class PaymentPlanInvesmentInline(admin.TabularInline):
    model = PaymentPlans


class InvestmentPlanInline(admin.TabularInline):
    model = InvestmentPlans


class AmenitieInline(admin.TabularInline):
    model = Amenitie


class OffPlaneInvesmentInline(admin.ModelAdmin):
    inlines = [GalleryInline, AmenitieInline, InvestmentPlanInline, PaymentPlanInvesmentInline]


admin.site.register(OFFPlanAndInvestment, OffPlaneInvesmentInline)
