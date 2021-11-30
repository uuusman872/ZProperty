from django.contrib import admin
from .models import Question, PropertyInquiry


# Register your models here


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "posted_date"]


class PropertyInquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "posted_date", "property_name"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(PropertyInquiry, PropertyInquiryAdmin)