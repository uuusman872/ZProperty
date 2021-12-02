from django.shortcuts import render
from Agents.models import Agent


# Create your views here.

def agents(request):
    agents_list = Agent.objects.all()
    context = {
        "agent_list": agents_list
    }
    return render(request, "agents.html", context=context)
