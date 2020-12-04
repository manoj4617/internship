from django.urls import path , include
from  . import views


app_name = 'edutech_app'

urlpatterns = [
    path("", views.index, name="index"),
]

