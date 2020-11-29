"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.response import Response
from .views import *


urlpatterns = [
    path('activation_status/', activation_status_view),
    path('address_detail/', address_detail_view),
    path('qualification_data/', qualification_data_view),
    path('bank_details/', bank_details_view),
    path('personal_details/', personal_details_view),
    path('job_exp/', job_exp_view),
]
