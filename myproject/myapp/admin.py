from django.contrib import admin
from .models import Subjects
from .models import Klass
from .models import Teacher

admin.site.register(Subjects)
admin.site.register(Klass)
admin.site.register(Teacher)


