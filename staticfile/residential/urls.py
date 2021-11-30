from django.urls import path
from . import views

urlpatterns = [
    path('property-grid', views.propertyGrid, name='property-grid'),
    path('property-detail/<int:id>', views.propertyDetail, name='property-detail'),
]
