from django.contrib import admin
from .models import Agent


# Register your models here.

class AgentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "uploaded_date"]


admin.site.register(Agent, AgentAdmin)
