from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View


class LoginView(View):
    def get(self, request):
        return render(request, 'teleconsultoria/login.html', locals())

    def post(self, request):
        if request.POST.get('username') and request.POST.get('password'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('painel_view')
        return redirect('login_view')


class PainelAdminView(View):
    def get(self, request):
        return render(request, 'teleconsultoria/painel_admin.html', locals())
