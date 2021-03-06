from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.index, name="index"),
    path('create_cli/', views.createCLI, name="create_cli"),
    path('create_form/', views.create_form, name="create_form"),
]
