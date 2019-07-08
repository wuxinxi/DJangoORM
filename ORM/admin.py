from django.contrib import admin

from ORM.models import Teacher
from ORM.models import Course
from ORM.models import Student


# Register your models here.
class MyAdmin(admin.ModelAdmin):
   pass


admin.site.register(Teacher, MyAdmin)
admin.site.register(Course, MyAdmin)
admin.site.register(Student, MyAdmin)
