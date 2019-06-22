from    django.urls import path
from . import views
urlpatterns =[
    path('', views.sip_index, name='sip.index'),
    path('store_user', views.sip_store, name='add_sip_user')
]