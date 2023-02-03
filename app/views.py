from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

#Página inicial
def home(request):
    return render(request, 'home.html')

#formulário de cadastro
def create(request):
    return render(request, 'create.html')

#insersão dos dasos dos usuarios no banco
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'],request.POST['emeil'],request.POST['password'])
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'create.html',data)

#formulário do painel de login
def painel(request):
    return render(request, 'painel.html',)


#processar o login
def dologin(request):
    data = {}
    user = authenticate(username = request.POST['user'], password = request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou snha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)
    

#Página inicial do dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')