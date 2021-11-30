from django.urls import path
from . import views

urlpatterns = [
    path('offplan', views.offplan, name='offplan'),
    path('offplandetail/<int:planid>', views.offplandetail, name='offplandetail'),
]
