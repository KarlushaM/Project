from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher, Subjects, Klass
from django.views.generic import DetailView, ListView, View, CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin


def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))


class TeachersListViews(ListView):
	model = Teacher
	template_name = "teachers/teachers_list.html"
	context_object_name = "teachers"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['subjects'] = Subjects.objects.all()
		context['klasses'] = Klass.objects.all()
		return context

class TeachersDetailsView(DetailView):
	model = Teacher
	template_name = "teachers/teacher_details.html"
	context_object_name = "teacher"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		teacher = self.get_object()
		context['reviews'] = teacher.reviews.all().order_by('-created_at')
		context['form'] = ReviewForm()
		return context
	
	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			from django.urls import reverse
			return redirect(f"{reverse('login')}?next={request.path}")
		
		teacher = self.get_object()
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = form.save(commit=False)
			review.teacher = teacher
			review.user = request.user
			review.save()
			return redirect('teacher_details', pk=teacher.pk)
		else:
            # Если форма невалидна — рендерим страницу с ошибками
			context = self.get_context_data()
			context['form'] = form
			return render(request, self.template_name, context)
	

class TeacherFormView(LoginRequiredMixin, CreateView):
    model = Teacher
    fields = ('fio', 'photo', 'description', 'price', 'subjects', 'klass', 'phone',)
    template_name = 'teachers/teacher_form.html'

    def form_valid(self, form):
        # Привязываем текущего пользователя к объявлению
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Перенаправляем на страницу "Мои объявления"
        return reverse_lazy('my_ads')
	
class MyAdsView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers/my_ads.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        return Teacher.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subjects.objects.all()
        context['klasses'] = Klass.objects.all()
        print(context)
        return context
    

