from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from apps.auths.forms.login import LoginForm
from django.views.generic import TemplateView, View
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy



class LoginView(TemplateView):
    template_name = 'auths/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Cambia 'home' por la URL de destino
        return render(request, self.template_name, {'form': form})


class LogoutView(TemplateView):
    template_name = 'auths/logout.html'

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')


class ChangePasswordView(PasswordChangeView):
    template_name = 'auths/change_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('/')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
