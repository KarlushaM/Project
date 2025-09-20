from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматически входим после регистрации
            return redirect('teachers_list')  # или 'profile', если есть
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})

class ForceLogoutView(View):
    def post(self, request):
        logout(request)
        messages.success(request, "Вы успешно вышли из системы.")
        return redirect('teacher_list')

    def get(self, request):
        logout(request)
        messages.success(request, "Вы успешно вышли из системы.")
        return redirect('teacher_list')


