from django.contrib import admin
from .models import OfPlaneInvesments, OffPlanGallery
# Register your models here.

class GalleryInline(admin.TabularInline):
    model = OffPlanGallery


class OfPlaneInvesmentInline(admin.ModelAdmin):
    inlines = [GalleryInline]

admin.site.register(OfPlaneInvesments, OfPlaneInvesmentInline)
