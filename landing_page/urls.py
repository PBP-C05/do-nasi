from django.urls import path
from .views import landing_page, register, login_page, logout_view, get_json_penyalur

app_name = 'landing_page'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('register/', register, name='register'), 
    path('login/', login_page, name='login'),
    path('logout/', logout_view, name='logout'),
    path('penyalur-json/', get_json_penyalur, name = 'get_json_penyalur')
]