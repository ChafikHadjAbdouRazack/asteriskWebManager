from    django.urls import path
from . import views
urlpatterns =[
    path('', views.sip_index, name='sip.index')
]