from django.shortcuts import render, redirect
from offsure.models import OFFPlanAndInvestment
from residential.models import ResidentialProperties
from Agents.models import Agent
from Accounts.forms import QuestionForm
from django.contrib import messages
from django.db import DataError


# Create your views here.

def index(request):
    off_plan_properties = OFFPlanAndInvestment.objects.all().order_by('uploaded_date')
    all_res_properties = ResidentialProperties.objects.all().order_by('uploaded_date')
    agents = Agent.objects.all()[:3]
    context = {
        "offplan_all_properties": off_plan_properties,
        "all_res_properties": all_res_properties,
        "agents": agents,
    }
    return render(request, "index.html", context)


def contact(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.save()
            messages.success(request, "Question posted you will soon hear from us")
            return redirect("contact")
    form = QuestionForm()
    context = {
        "form": form
    }
    return render(request, "contact.html", context)


def about(request):
    agents = Agent.objects.all()[:3]
    context = {
        "agents": agents
    }
    return render(request, "about.html", context)
