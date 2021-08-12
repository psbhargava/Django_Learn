"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from testapp.views import date_time_view, hello_world_view
# from greetapp import views
from testapp import views as v1
from greetapp import views as v2


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^testapp/', include('testapp.urls')),
    url(r'^hello/', v1.hello_world_view),
    url(r'^datetime/', v1.date_time_view),
    url(r'^morning/', v2.good_morning),
    url(r'^afternoon/', v2.good_afternoon),
    url(r'^evening/', v2.good_evening),
    url(r'^night/', v2.good_night),
]
