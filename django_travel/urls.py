"""django_travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import django_travel_data.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.button),
    path(r'output1/', views.output1, name='script1'),
    path(r'output2/', views.output2, name='script2'),
    path(r'output3/', views.output3, name='script3'),
    path(r'output4/', views.output4, name='script4'),
    path(r'output5/', views.output5, name='script5'),

]
