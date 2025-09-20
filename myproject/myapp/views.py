from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher
from django.views.generic import DetailView, ListView, View, CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))


class TeachersListViews(ListView):
	model = Teacher
	template_name = "teachers/teachers_list.html"
	context_object_name = "teachers"

class TeachersDetailsView(DetailView):
	model = Teacher
	template_name = "teachers/teacher_details.html"
	context_object_name = "teacher"
	

class TeacherFormView(CreateView):
	model = Teacher
	fields = "__all__"
	template_name ='teachers/teacher_form.html'
	def get_success_url(self):
		return reverse("teacher_details", kwargs={"pk":self.object.pk})
	


