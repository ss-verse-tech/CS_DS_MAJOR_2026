from django.contrib import admin
from to_do_list_app.models import To_Do_List
# Register your models here.
@admin.register(To_Do_List)
class Show_To_Do_List(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'done', 'created')