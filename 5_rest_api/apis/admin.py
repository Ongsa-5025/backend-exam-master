from django.contrib import admin

# Register your models here.

from .models import School
from .models import ClassRoom
from .models import Teacher
from .models import Student


admin.site.register(School)
admin.site.register(ClassRoom)
admin.site.register(Teacher)
admin.site.register(Student)