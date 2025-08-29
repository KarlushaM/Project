from django.contrib import admin
from .models import Subjects
from .models import Klass
from .models import Teachers

admin.site.register(Subjects)
admin.site.register(Klass)
admin.site.register(Teachers)


# Register your models here.
