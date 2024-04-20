"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from users import views as users




urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',users.index,name='index'),
    path('idor_page/',users.idor_page,name='idor_page'),
    path('Sqli_page/',users.Sqli_page,name='Sqli_page'),
    path('Otpbp_page/',users.Otpbp_page,name='Otpbp_page'),
     path('xss_page/',users.xss_page,name='xss_page'),
   path('Htmli_page/',users.Htmli_page,name='Htmli_page'),
   path('ssrf_page/',users.ssrf_page,name='ssrf_page'),
    path('hhi_page/',users.hhi_page,name='hhi_page'),
     path('pt_page/',users.pt_page,name='pt_page'),
]
