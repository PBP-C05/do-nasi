import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from harapan_page.models import HarapanDonatur
from landing_page.models import Pengguna
from django.contrib import messages
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.utils import timezone



# @login_required(login_url='/login/')
# @csrf_exempt
# def show_harapan(request):
#   if request.user.is_authenticated:
#        role = request.user.role
#        if role == "Penyalur":
#            pengguna = Pengguna.objects.get(username=request.user.username)
#            data_harapan = HarapanDonatur.objects.filter(user=pengguna)
#            context = {
#                'roles': True,
#               'data_harapan': data_harapan,
#            }
#            return render(request, "harapan_page.html", context)
#        else:
#            data_harapan = HarapanDonatur.objects.all()
#            context = {
#                'roles': False,
#                'data_harapan': data_harapan,
#            }
#            return render(request, "harapan_page.html", context)
#    else:
#        return redirect('landing_page:login')

def show_harapan(request):
    if request.user.is_authenticated:
        data_harapan = HarapanDonatur.objects.all()
        context = {
            'data_harapan': data_harapan,
        }
        return render(request, "harapan_page.html", context)
    else:
        return redirect('landing_page:login')


@login_required(login_url='/login/')
@csrf_exempt
def harapan_page(request):
    if request.method == 'POST':
        user = request.user
        text = request.POST.get('text')
        if  text is None:
            data = json.loads(request.body)
            text = data['text']
        if text is not None:
            item = HarapanDonatur.objects.create(
                user=user, text=text, username=user, email=user.get_email())
            item.save()
        # HarapanDonatur.objects.all().delete()
            return JsonResponse({'message': 'Harapan Created!', 'error': False})
    """if request.method == 'POST':
        # retrieving data
        pengguna = request.user
        judul = request.POST.get('title')
        isi = request.POST.get('body')
        created_at = timezone.now()
        text = request.POST.get('text')
        
        # making new instance and saving it
        harapan = HarapanDonatur(
            user = pengguna,
            #title = judul,
            created_at = created_at,
            text = text
        )
        harapan.save()
        
        return JsonResponse({
            "pk": harapan.pk,
            "fields": {
                "user":  harapan.user.username,
                "username": harapan.user.username,
                "email": harapan.user.email,
                "created_at": harapan.created_at,
                "text": harapan.text
            }
        })
"""

@csrf_exempt
def show_harapan_json(request):
    data = HarapanDonatur.objects.all()


    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )
    """data = []
    allHarapan = HarapanDonatur.objects.all()
    print(allHarapan)

    for harapan in allHarapan:
        data.append({
            "pk": harapan.pk,
            "fields": {
                "user" : { 
                        "username" : harapan.user.username,
                        "name"     : harapan.user.name,
                        "role"     : harapan.user.role
                        },
                "username": harapan.user.username,
                "email": harapan.user.email,
                "created_at": harapan.created_at.strftime("%B %d, %Y at %H:%M %Z"),
                "text": harapan.text
            }
        })
    return JsonResponse(data, safe=False)"""


@login_required(login_url='/login/')
@csrf_exempt
def delete_ajax(request, key):
    if request.method == 'POST':
        mytask = get_object_or_404(HarapanDonatur, user=request.user, pk=key)
        mytask.delete()

    return JsonResponse({'error': False})
