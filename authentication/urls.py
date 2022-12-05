from django.urls import path
from .views import login, register, logout, get_user

app_name = 'authentication'

urlpatterns = [
    path('login_flutter/', login, name='login_flutter'),
    path('signup_flutter/', register, name='signup_flutter'),
    path('logout_flutter/', logout, name='logout_flutter'),
    path('user/', get_user, name='user')
]
