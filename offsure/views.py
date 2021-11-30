from django.shortcuts import render, redirect
from Accounts.forms import PropertyInquiryForm
from offsure.models import OFFPlanAndInvestment
from offsure.models import OffPlanGallery, PaymentPlans, Amenitie, InvestmentPlans
from django.contrib import messages


# Create your views here.

def offplan(request):
    plans_list = OFFPlanAndInvestment.objects.all()
    context = {
        "plans_list": plans_list
    }
    return render(request, "off-plan.html", context=context)


def offplandetail(request, planid):
    plan_detail = OFFPlanAndInvestment.objects.get(id=planid)
    headerImages = OffPlanGallery.objects.filter(plan=plan_detail)
    paymentPlans = PaymentPlans.objects.filter(plan=plan_detail)
    invesmentPlans = InvestmentPlans.objects.filter(plan=plan_detail)
    amentites = Amenitie.objects.filter(property=plan_detail)
    if request.method == "POST":
        form = PropertyInquiryForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.property_type = "Off plan"
            newform.property_name = plan_detail.Title
            newform.save()
            messages.success(request, "Question posted you will soon hear from us")
            return redirect('offplandetail', planid)
    form = PropertyInquiryForm()
    context = {
        "plan_detail": plan_detail,
        "Galleries": headerImages,
        "invesments": invesmentPlans,
        "paymentPlans": paymentPlans,
        "amentites": amentites,
        "form": form
    }
    return render(request, "off-plan-detail.html", context=context)
