from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher
from .forms import TeacherForm

def teachers_list(request):
		teachers = Teacher.objects.all()
		form = TeacherForm()
		return render(request, 'teachers/teachers_list.html', {"teachers": teachers, "form": form})

