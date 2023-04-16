from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('testarm', views.testarm, name='testarm'),
    path('testarm1', views.testarm1, name='testarm1'),
]
