from django.urls import path
from .views import login, register, logout, get_user

app_name = 'authentication'

urlpatterns = [
    path('login_flutter/', login, name='login_flutter'),
    path('register_flutter/', register, name='register_flutter'),
    path('logout_flutter/', logout, name='logout_flutter'),
    path('get_user_json/', get_user, name='get_user_json'),
]
