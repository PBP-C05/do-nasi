from django.urls import path
from page_overview.views import *

app_name = 'page_overview'

urlpatterns = [
    path('', show_overview, name='show_overview'),
    path('add/', add_donasi_ajax, name = 'add_donasi_ajax'),
    path('json/', get_json, name = 'get_json'),
    path('donate/<int:id>', do_donation, name='do_donation'),
    path('json-flutter/', get_json_flutter, name = 'get_json-flutter')
]