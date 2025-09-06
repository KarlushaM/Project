from django.urls import path
from . import views
from .views import ForceLogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', ForceLogoutView.as_view(), name='logout'),  # 👈 перехватываем выход
]

urlpatterns = [
    path('register/', views.register, name='register'),
]