"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#from jet.dashboard.dashboard_modules import google_analytics_views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^', include('blog.urls')),
    url(r'^', include('blog.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin.site.urls),
]

admin.site.site_header = "NAPI Admin"
admin.site.site_title = "NAPI Admin Portal"
admin.site.index_title = "NAPI | bem vindo ao Portal"