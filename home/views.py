from django.shortcuts import render,redirect
from home .models import *
# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def registerpage(request):
    
    if request.method == 'POST':
        userv = request.POST.get('usernameh')
        emailv = request.POST.get('emailh')
        passv = request.POST.get('passwordh')
        imgv = request.FILES.get('imgh')

        insert = Userdata(username = userv, email = emailv, password = passv, image = imgv)
        insert.save()
        
        return redirect('displaypage')
    return render(request, 'register.html')

def display(request):
    read = Userdata.objects.all()
    if request.GET.get('search'):
        read = read.filter(username__icontains = request.GET.get('search'))
    context = {'readdata':read}

    return render(request, 'display.html', context)

def loginpage(request):
    return render(request, 'login.html')

def update_user(request, id):
    user = Userdata.objects.get(id = id)
    if request.method == "POST":
        user.username = request.POST.get('usernameh')
        user.email = request.POST.get('emailh')
        user.password = request.POST.get('passwordh')
        user.save()
        return redirect('displaypage')
    return render(request, 'update.html', {'userinfo': user})

def delete(request, id):
    dltuser = Userdata.objects.get(id = id)
    dltuser.delete()
    return redirect('displaypage')