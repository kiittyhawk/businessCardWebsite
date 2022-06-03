from django.http import HttpResponse
from typing import Any, Dict
from django.urls import reverse_lazy
from ..forms.login import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm


    def form_valid(self, form: LoginForm) -> HttpResponse:
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is None:
            messages.error(self.request, 'Invalid username or password')
            return
        login(self.request, user)
        messages.info(self.request, f'You are now logged in as {username}')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('index')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
