from django.contrib import admin
from django.urls import path
from gee import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home.as_view(), name="home"),

]
