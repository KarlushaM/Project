from django.urls import path
from .views import TeachersListViews, TeachersDetailsView, TeacherFormView, MyAdsView
from . import views

urlpatterns = [
		path('', TeachersListViews.as_view(), name = "teachers_list"),
        path('create/', TeacherFormView.as_view(), name = "create_teacher"), 
        path('<int:pk>/', TeachersDetailsView.as_view(), name = "teacher_details"),
        path('logout/', views.logout_view, name='logout'),
        path('my-ads/', MyAdsView.as_view(), name='my_ads'),
]