from django.shortcuts import render, redirect
from Accounts.forms import PropertyInquiryForm
from residential.models import ResidentialProperties, ResidentialPropertiesImage, Amenitie, PaymentPlans, InvestmentPlans
from django.contrib import messages


def propertyGrid(request):
    all_properties = ResidentialProperties.objects.all()
    context = {
        "all_prop": all_properties,
    }
    return render(request, "property-grid.html", context=context)

#
# def processInquiryForm(request, id):
#     plan = ResidentialProperties.objects.filter(id=id)[0]
#     if request.method == "POST":
#         form = PropertyInquiryForm(request.POST or None)
#         if form.is_valid():
#             newform = form.save(commit=False)
#             newform.property_type = "Residential"
#             newform.property_name = plan.Title
#             form.save()
#             messages.success(request, "Question posted you will soon hear from us")
#             return redirect("property-detail", id=id)


def propertyDetail(request, id):
    plan = ResidentialProperties.objects.filter(id=id)[0]
    gallery = ResidentialPropertiesImage.objects.filter(property=plan)
    amanities = Amenitie.objects.filter(property=plan)
    paymentPlans = PaymentPlans.objects.filter(plan=plan)
    invesmentPlans = InvestmentPlans.objects.filter(plan=plan)
    if request.method == "POST":
        form = PropertyInquiryForm(request.POST or None)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.property_type = "Residential"
            newform.property_name = plan.Title
            form.save()
            messages.success(request, "Question posted you will soon hear from us")
            return redirect("property-detail", id=id)
    form = PropertyInquiryForm()
    context = {
        "plan_detail": plan,
        "Galleries": gallery,
        "amentites": amanities,
        "paymentPlans": paymentPlans,
        "invesments": invesmentPlans,
        "form": form
    }
    return render(request, "property-detail.html", context)
