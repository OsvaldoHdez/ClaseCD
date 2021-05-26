from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url = "http://127.0.0.1:8000/home/v2/detail_client/6/"
    response = requests.get(url)
    context = {
        "obj": response.json()
    }
    return render(request, "home/index.html", context)

def createCLI(request):
    url = "http://127.0.0.1:8000/home/v1/clients"
    payload = ("datos usuario aquí separados por una coma ','")# podemos enviar field forms, obj, etc
    response = requests.post(url, data=payload)
    context = {
        "message": "Correcto"
    }
    return render(request, "home/create_cli.html", context)

def create_form(request):
    phone = request.GET("phone")
    user = request.GET("user")
    status = request.GET("status")
    if status == "on":
        status = True
    else: 
        status = False
    payload = {"phone": phone, "status": status, "user": user}
    print(payload)
    # print("{0}-{1}-{2}".format(phone, user, status))
    url = "http://127.0.0.1:8000/home/v1/clients"
    response = requests.post(url, data=payload)
    context = {
        "message": response.status_code
    }
    return render(request, "home/create_form.html", context)