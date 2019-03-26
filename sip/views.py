from django.shortcuts import render
from django.http import HttpResponse
import telnetlib
# Create your views here.

def index (request):

   return render(request,'sip/page-login.html')


def login(request):
   HOST = "192.168.1.2"
   PORT = "5038"

   tn = telnetlib.Telnet(HOST, PORT)
   tn.write(b'Action:Login\r\n')
   tn.write(b'Username:master\r\n')
   tn.write(b'Secret:razack\r\n')
   tn.write(b'\r\n')
   tn.write(b'Action:LogOff\r\n')
   tn.write(b'\r\n\r\n')
   response = tn.read_all()
   response = response.decode("UTF-8")
   print(response)
   resp = "Authentication accepted" in response
   print(resp)
   pass