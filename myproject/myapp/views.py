from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher
from django.views.generic import DetailView, ListView, View, CreateView
from django.urls import reverse_lazy, reverse

class TeachersListViews(ListView):
	model = Teacher
	template_name = "teachers/teachers_list.html"
	context_object_name = "teachers"

class TeachersDeatailsView(DetailView):
	model = Teacher
	template_name = "teachers/teacher_deatails.html"
	context_object_name = "teacher"

class TeacherFormView(CreateView):
	model = Teacher
	fields = "__all__"
	template_name ='teachers/teacher_form.html'
	def get_success_url(self):
		return reverse("teacher_deatails", kwargs={"pk":self.object.pk})
	


