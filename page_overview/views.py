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
def add_donasi_ajax(request):
    if request.user.is_authenticated:
        form = create_form(request.POST)
        data = {}   
        if request.method == 'POST' and form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            deadline = form.cleaned_data['deadline']
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

def do_donation(request, id):
    if request.user.is_authenticated:
        donate = Donasi.objects.get(id=id)
        donate.Donation = True
        donate.save()
        return JsonResponse({'msg':'success'})
    else:
        return redirect('landing_page:login')