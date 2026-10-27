from django.contrib import admin
from DB_Learning.models import Student
# Register your models here.
# admin.site.register(Student)
@admin.register(Student)
class Student_data(admin.ModelAdmin):
    list_display = ('name','age', 'department','date')
    search_fields = ("name",'age')
    list_filter = ('name','age')