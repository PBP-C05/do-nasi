from django.conf.urls import url
from .views import login, register, logout, get_user

app_name = 'authentication'

urlpatterns = [
    url('login_flutter/', login, name='login_flutter'),
    url('signup_flutter/', register, name='signup_flutter'),
    url('logout_flutter/', logout, name='logout_flutter'),
    url('user/', get_user, name='user')
]
