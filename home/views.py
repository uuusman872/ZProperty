from django.shortcuts import render
from offsure.models import OFFPlanAndInvestment, OffPlanGallery
# Create your views here.


def index(request):
    plan = OFFPlanAndInvestment.objects.get(id=5)
    dImage = plan.Dashboard_Image.url
    images = OffPlanGallery.objects.filter(plan=plan)
    print("[+] The images are ", images)
    print("[+] The dashboard image path is ", dImage)
    context = {
        "dImage": dImage
    }
    return render(request, "index.html", context=context)