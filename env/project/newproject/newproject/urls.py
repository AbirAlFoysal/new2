from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from newapp import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('newapp.urls')),

]
