from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('car_details/<int:id>/', views.car_details, name='car_details'),
    
]