from django.shortcuts import render,redirect
from .models import *
import json
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
import time
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required



API_URL = "https://api-inference.huggingface.co/models/google/tapas-base-finetuned-wtq"
headers = {"Authorization": "Bearer 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"}

def query_database_func(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

# Create your views here.

@staff_member_required
def index (request):
    data = logs.objects.filter(user_name = request.user.username)
    data2 = dataset.objects.filter(user_name = request.user.username,user_id = request.user.id)
    date = logs.objects.filter(user_name = request.user.username).values_list("date",flat=True)
    date = [date_object.strftime('%Y-%m-%d %H:%M:%S') for date_object in date]
    response_time = logs.objects.filter(user_name = request.user.username).values_list("response_time",flat=True)
    response_time = [float(time) for time in response_time]
    # print("=====",response_time)
    return render(request , "index.html",{"data":data , "data2":data2 , "date":date , "response_time":response_time})


def datasets (request):
    data = dataset.objects.filter(user_name = request.user.username,user_id = request.user.id)
    return render(request , "datasets.html",{"data":data})


def developers (request):
    return render(request , "developers.html")

@csrf_exempt
def query (request,uuid):

    if request.method == 'POST':
        dict_data = json.loads(request.body.decode('UTF-8'))
        user = authenticate(request, username=dict_data["username"], password= dict_data["password"]) 
        if user is not None:
            start_time = time.time()
            data = (dataset.objects.filter(uuid = uuid).first())
            query_ = dict_data["query"]
            output = query_database_func({
                "inputs": {
                    "query": query_,
                    "table": json.loads(data.data)
                },
            })
            end_time = time.time()
            logs.objects.create(data_uuid = data.uuid , query = query_ , user_name = dict_data["username"], answer = output['answer'], response_time = round((end_time - start_time) * 1000, 2) )
            print("========",request.user.username ,request.user.id )
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



def login_v(request):
    return render(request , "login.html")
    