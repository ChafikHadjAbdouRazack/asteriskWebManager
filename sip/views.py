from django.shortcuts import render, redirect
from django.http import HttpResponse
import telnetlib, psutil
# Create your views here.

def index (request):

   return render(request,'sip/page-login.html')


def login(request):
   HOST = "192.168.1.2"
   PORT = "5038"
   tn = telnetlib.Telnet(HOST, PORT)
   user = 'Username:'+request.POST['username']
   secret = 'Secret:'+request.POST['password']
   tn.write(b'Action:Login\r\n')
   tn.write(user.encode('ascii')+b'\r\n')
   tn.write(secret.encode('ascii')+b'\r\n')
   tn.write(b'\r\n')
   tn.write(b'Action:LogOff\r\n')
   tn.write(b'\r\n\r\n')
   response = tn.read_all()
   response = response.decode("UTF-8")
   print(response)
   resp = "Authentication accepted" in response
   print(resp)
   if resp :
      return redirect('dashboard')
   else:
      return redirect('login')

def dashboard(request):
   context = {
      'pourcentage':int(psutil.virtual_memory()[2])
   }
   return render(request,'sip/index.html', context)


def sip_index(request):
   pass

def sip_create(request):
   pass

def sip_store(request):
   pass
