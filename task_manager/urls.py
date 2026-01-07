from django.contrib import admin
from django.urls import path
from tasks.views import task_view, add_task_view, delete_task_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', task_view),
    path('', task_view),
    path('task/add-task', add_task_view),
    path('task/delete-task/<int:index>', delete_task_view)  # Home page mapped to task_view
]