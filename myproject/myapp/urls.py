from django.urls import path
from .views import TeachersListViews, TeachersDeatailsView, TeacherFormView

urlpatterns = [
		path('', TeachersListViews.as_view(), name = "teachers_list"),
        path('create/', TeacherFormView.as_view()), 
        path('<int:pk>/', TeachersDeatailsView.as_view(), name = "teacher_deatails"),
]