from django.contrib import admin
from .models import OFFPlanAndInvestment, OffPlanGallery, PaymentPlans
# Register your models here.


class GalleryInline(admin.TabularInline):
    model = OffPlanGallery


class PaymentPlanInvesmentInline(admin.TabularInline):
    model = PaymentPlans


class OffPlaneInvesmentInline(admin.ModelAdmin):
    inlines = [GalleryInline, PaymentPlanInvesmentInline]


admin.site.register(OFFPlanAndInvestment, OffPlaneInvesmentInline)
