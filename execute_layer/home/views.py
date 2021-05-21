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