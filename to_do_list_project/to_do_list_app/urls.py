from django.urls import path
from to_do_list_app import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("add_task/", views.add_task, name = "add_task"),
    path('edit_task/<int:id>', views.edit_task, name = "edit_task")
   
]
