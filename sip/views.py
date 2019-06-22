from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
import telnetlib, psutil, shlex, subprocess, os


# Create your views here.

def index(request):
    return render(request, 'sip/page-login.html')


def login(request):
    HOST = "127.0.0.1"
    PORT = "5038"
    user = ""
    secret = ""
    tn = telnetlib.Telnet(HOST, PORT)
    if request.method == 'GET':
        data = request.GET
        user = 'Username:' + data['username']
        secret = 'Secret:' + data['password']
    elif request.method == 'POST':
        data = request.POST
        user = 'Username:' + data['username']
        secret = 'Secret:' + data['password']
    tn.write(b'Action:Login\r\n')
    tn.write(user.encode('ascii') + b'\r\n')
    tn.write(secret.encode('ascii') + b'\r\n')
    tn.write(b'\r\n')
    tn.write(b'Action:LogOff\r\n')
    tn.write(b'\r\n\r\n')
    response = tn.read_all()
    response = response.decode("UTF-8")
    resp = "Authentication accepted" in response
    if resp:
        return redirect('dashboard')
    else:
        return redirect('connexion')


def dashboard(request):
    cmd = shlex.split("sudo /usr/sbin/asterisk -rx 'core show uptime'")
    command = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = command.communicate()
    uptime = stdout.decode('UTF-8')
    cmd = shlex.split("sudo /usr/sbin/asterisk -rx 'sip show peers'")
    command = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = command.communicate()
    entete = list(filter(None, stdout.decode('UTF-8').split('\n')[0].split(' ')))
    result = stdout.decode('UTF-8').split('\n')
    result.pop(0)
    result.pop()
    stat = result.pop()
    sips = []
    for element in result:
        elet = list(filter(None, element.split(' ')))
        sips.append({
            'name': elet[0],
            'hote': elet[1],
            'port': elet[6],
            'status': elet[7]
        })
    context = {
        'uptime': uptime,
        'pourcentage': int(psutil.virtual_memory()[2]),
        'processeur': int(psutil.cpu_percent()),
        'sip': sips,
        'stat': stat
    }
    return render(request, 'sip/index.html', context)


def sip_index(request):
    cmd = shlex.split("sudo /usr/sbin/asterisk -rx 'sip reload'")
    command = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = command.communicate()
    cmd = shlex.split("sudo /usr/sbin/asterisk -rx 'sip show peers'")
    command = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = command.communicate()
    entete = list(filter(None, stdout.decode('UTF-8').split('\n')[0].split(' ')))
    result = stdout.decode('UTF-8').split('\n')
    result.pop(0)
    result.pop()
    stat = result.pop()
    sips = []
    for element in result:
        elet = list(filter(None, element.split(' ')))
        sips.append({
            'name': elet[0],
            'hote': elet[1],
            'port': elet[6],
            'status': elet[7]
        })
    context = {
        'sip': sips,
        'stat': stat
    }
    return render(request, 'sip/sip.html', context)


def sip_store(request):
    sip_user_info = "\n[{}](default_template) \nfullname ={} \nusername ={} \nsecret={} \nmailbox ={} \ncontext=dept_1".format(request.POST['extension'],request.POST['full_name'], request.POST['username'],request.POST['password'],request.POST['extension'])
    os.system("sudo bash -c 'echo \"{}\" >> /etc/asterisk/users.conf'".format(sip_user_info))
    cmd = shlex.split("sudo /usr/sbin/asterisk -rx 'sip reload'")
    command = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = command.communicate()
    return redirect('sip.index')
