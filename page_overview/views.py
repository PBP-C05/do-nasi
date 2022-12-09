from multiprocessing import Event
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from django.core import serializers
from page_overview.models import Donasi
from page_overview.forms import create_form
from landing_page.models import Pengguna
from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.

@login_required(login_url='/landing_page/login/')
def show_overview(request):
    if request.user.is_authenticated:
        role = request.user.role
        if role == "Penyalur":
            pengguna = Pengguna.objects.get(username = request.user.username)
            list = Donasi.objects.filter(user = pengguna)
            context = {
                'roles': True,
                'user_donasi': list,
            }
            return render(request, "page_overview.html", context)
        else:
            list = Donasi.objects.all()
            context = {
            'roles': False,
            'user_donasi': list,
            }
            return render(request, "page_overview.html", context)
    else:
       return redirect('landing_page:login') 

@login_required(login_url='/landing_page/login/')
@csrf_exempt
def add_donasi_ajax(request):
    if request.user.is_authenticated:
        form = create_form(request.POST)
        data = {}   
        if request.method == 'POST' and form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            deadline = form.cleaned_data['deadline']
            try :
                deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S.%f").date()
                deadline = deadline.strftime("%Y-%m-%d")
            except :
                deadline = deadline
            new_task = Donasi.objects.create(title=title, description=description, user=request.user, deadline = deadline)
            data['title'] = title
            data['description'] = description
            # data['user'] = request.user
            data['deadline'] = deadline
            return JsonResponse(data)
    else:
        return redirect('landing_page:login')

def get_json(request):
    role = request.user.role
    if role == "Penyalur":
        pengguna = Pengguna.objects.get(username = request.user.username)
        list = Donasi.objects.filter(user = pengguna)
        return HttpResponse(serializers.serialize("json", list), content_type="application/json")
    else :
        list = Donasi.objects.all()
        return HttpResponse(serializers.serialize("json", list), content_type="application/json")

def get_json_flutter(request):
    role = request.user.role
    response_data = {}
    if role == "Penyalur":
        pengguna = Pengguna.objects.get(username = request.user.username)
        response_data["user"] = json.loads(serializers.serialize("json", [pengguna]))
        list = Donasi.objects.filter(user = pengguna)
        response_data['data'] = json.loads(serializers.serialize("json", list))
        return JsonResponse((response_data))
    else :
        pengguna = Pengguna.objects.get(username = request.user.username)
        response_data["user"] = json.loads(serializers.serialize("json", [pengguna]))
        list = Donasi.objects.all()
        response_data['data'] = json.loads(serializers.serialize("json", list))
        return JsonResponse((response_data))

def do_donation(request, id):
    if request.user.is_authenticated:
        donate = Donasi.objects.get(id=id)
        donate.Donation = True
        donate.save()
        return JsonResponse({'msg':'success'})
    else:
        return redirect('landing_page:login')