from django.urls import path
from buddytask.views import tasklist, contact, home,delete_task, edit_task , complete_task, notcomplete_task

urlpatterns = [
    path('tasklist', tasklist, name='tasklist'),
   
    path('delete/<task_id>', delete_task, name= "delete_task"),
    path('edit/<task_id>', edit_task, name= "edit_task"),
    path('complete/<task_id>', complete_task, name = 'complete_task'),
    path('notcomplete/<task_id>', notcomplete_task, name = 'notcomplete_task'),
]
