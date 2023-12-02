from django.shortcuts import render,redirect
from .models import *
import json
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 



API_URL = "https://api-inference.huggingface.co/models/google/tapas-base-finetuned-wtq"
headers = {"Authorization": "Bearer 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"}

def query_database_func(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

# Create your views here.


def index (request):
    data = logs.objects.filter(user_name = request.user.username,user_id = request.user.id)
    data2 = dataset.objects.filter(user_name = request.user.username,user_id = request.user.id)
    return render(request , "index.html",{"data":data , "data2":data2})


def datasets (request):
    data = dataset.objects.filter(user_name = request.user.username,user_id = request.user.id)
    return render(request , "datasets.html",{"data":data})


def developers (request):
    return render(request , "developers.html")

@csrf_exempt
def query (request,uuid):

    if requests.method == 'POST':
        data = (dataset.objects.filter(uuid = uuid).first())
        dict_data = json.loads(requests.body.decode('UTF-8'))
        query_ = dict_data["query"]
        output = query_database_func({
            "inputs": {
                "query": query_,
                "table": json.loads(data.data)
            },
        })
        logs.objects.create(data_uuid = data.uuid , query = query_ , user_name = request.user.username , user_id = request.user.id , answer = output['answer'])
        print(requests.user.username)
        return HttpResponse(output['answer'])
    

def add_datasets(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        data = request.POST.get("data")
        dataset.objects.create(name = name , description = description , data = data , user_name = request.user.username , user_id = request.user.id)
        return redirect("/datasets")


def add_delete(request,uuid):
     dataset.objects.filter(uuid=uuid).delete()
     return redirect("/datasets")

