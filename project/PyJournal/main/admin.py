from django.contrib import admin

# Register your models here.
from main.models import Student, Teacher, Subject, Mark

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Mark)
