from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="jettybalance"),
    path('services/', services, name="services"),
    path('apply-now/', apply_now, name="apply-now"),
]