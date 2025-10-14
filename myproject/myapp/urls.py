
from .views import TeachersListViews, TeachersDetailsView, TeacherFormView, MyAdsView
from . import views
from django.urls import path, include

urlpatterns = [
		path('', TeachersListViews.as_view(), name = "teachers_list"),
        path('create/', TeacherFormView.as_view(), name = "create_teacher"), 
        path('<int:pk>/', TeachersDetailsView.as_view(), name = "teacher_details"),
        path('logout/', views.logout_view, name='logout'),
        path('my-ads/', MyAdsView.as_view(), name='my_ads'),
        path('teacher/<int:pk>/delete/', views.delete_teacher, name='delete_teacher'),
        path('teacher/<int:pk>/hide/', views.hide_teacher, name='hide_teacher'),
        path('teacher/<int:pk>/restore/', views.restore_teacher, name='restore_teacher'),
        path('teacher/<int:teacher_id>/status/<str:new_status>/', views.change_teacher_status, name='change_teacher_status'),
        path('moderation/', views.ModerationView.as_view(), name='moderation'),
        path('accounts/', include('django.contrib.auth.urls')),
]