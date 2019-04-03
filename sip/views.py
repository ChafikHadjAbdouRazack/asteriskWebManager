from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
import telnetlib, psutil
# Create your views here.

def index (request):

   return render(request,'sip/page-login.html')


def login(request):
   HOST = "127.0.0.1"
   PORT = "5038"
   user =""
   secret = ""
   tn = telnetlib.Telnet(HOST, PORT)
   if request.method == 'GET':
       data = request.GET
       user = 'Username:'+data['username']
       secret = 'Secret:'+data['password']
   elif request.method == 'POST':
       data = request.POST
       user = 'Username:' + data['username']
       secret = 'Secret:' + data['password']
   tn.write(b'Action:Login\r\n')
   tn.write(user.encode('ascii')+b'\r\n')
   tn.write(secret.encode('ascii')+b'\r\n')
   tn.write(b'\r\n')
   tn.write(b'Action:LogOff\r\n')
   tn.write(b'\r\n\r\n')
   response = tn.read_all()
   response = response.decode("UTF-8")
   resp = "Authentication accepted" in response
   if resp :
      return redirect('dashboard')
   else:
      return redirect('connexion')

def dashboard(request):
   context = {
      'pourcentage':int(psutil.virtual_memory()[2]),
      'processeur' : int(psutil.cpu_percent())
   }
   return render(request,'sip/index.html', context)


def sip_index(request):

   return render(request, 'sip/sip.html')


def sip_store(request):
   pass
