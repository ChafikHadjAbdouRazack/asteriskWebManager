from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):

   return render(request,'sip/page-login.html')


def login(request):
   pass