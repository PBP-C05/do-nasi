from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from landing_page.models import Pengguna


@csrf_exempt
def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def register(request):
    # if (request.method == "POST"):
    #     try:
    #         email = request.POST.get("email")
	# 		username = request.POST.get("username")
    #         password = request.POST.get("password")

    #         new_user = User.objects.create_user(email=email, username=username, password=password)
    #         new_user.save()
    #         new_user_profile = Pengguna.objects.create(user=new_user)
    #         return JsonResponse({"instance": "user Dibuat"}, status=200)
        
    #     except:
    #         return JsonResponse({"instance": "gagal Dibuat"}, status=400)
        
    return JsonResponse({"instance": "gagal Dibuat"}, status=400)


@csrf_exempt
def logout(request):
	if request.user.is_authenticated or ['loggedIn']:
		if request.user.is_authenticated:
			auth_logout(request)
		return JsonResponse({"status" : "logged out"}, status=200)
	return JsonResponse({"status": "Not yet authenticated"}, status =403)

@csrf_exempt
def get_user(request):
	if request.user.is_authenticated or ['loggedIn']:
		if request.user.is_authenticated:
			return JsonResponse({"status" : True, "data": 
            {"email": request.user.email, "username": request.user.username, 
	        "name": request.user.name, "role": request.user.role
            }}, status=200)
	return JsonResponse({"status": False}, status =403)