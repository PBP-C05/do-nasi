import json
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from landing_page.models import PenggunaManager, Pengguna

# Create your views here.
@csrf_exempt
def login(request):
	context = {}
	user = request.user
	
	if request.method == "POST":
		data = json.loads(request.body)
		email = data['email']
		password = data['password']
		user = authenticate(request, email=email, password=password)
		if user:
			login(request, user)
			context['login'] = "logged-in"
			context['user'] = {"email": user.email, "username": user.username, 
                                "name": user.name, "role": user.role, 
                                "is_admin": user.is_admin}
			return JsonResponse({'data': context}, status=200)

	context['login'] = 'unlogin'
	return JsonResponse({'data': context}, status=500)

@csrf_exempt
def register(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		email = data['email']
		username = data['username']
		password = data['password']
		name = data['name']
		
		try:
			new_user = Pengguna.objects.create_user(email, username, password)
			new_user.name = name
			new_user.save()
			return JsonResponse({"instance": "user Dibuat"}, status=200)
		except:
			return JsonResponse({"instance": "gagal Dibuat"}, status=400)

	return JsonResponse({"instance": "gagal Dibuat"}, status=400)

@csrf_exempt
def logout(request):
	data = json.loads(request.body)
	if request.user.is_authenticated or data['loggedIn']:
		if request.user.is_authenticated:
			logout(request)
		return JsonResponse({"status" : "loggedout"}, status=200)
	return JsonResponse({"status": "Not yet authenticated"}, status =403)

@csrf_exempt
def get_user(request):
	user = request.user
	if not user.is_authenticated:
		return JsonResponse({"result": "Not yet authenticated!"}, status=403)
	
	user = Pengguna.objects.get(username=user)
	return JsonResponse({"data": {"email": user.email, "username": user.username, 
	"name": user.name, "is_admin": user.is_admin}}, status=200)
