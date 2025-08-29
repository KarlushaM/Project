from django.urls import path
from .views import teachers_list

urlpatterns = [
		path('', teachers_list),
]