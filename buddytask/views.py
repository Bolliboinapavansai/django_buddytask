from django.shortcuts import render, redirect
from .models import TaskList
from .form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def tasklist(request):
    if request.method =="POST":
        form = TaskForm(request.POST or None) 
        if form.is_valid():
            form.save(commit=False).manage= request.user
            form.save()
            messages.success(request,("Task Added"))
        return redirect(tasklist)
    else:
        all_tasks = TaskList.objects.filter(manage=request.user)
        pagiantor = Paginator(all_tasks, 5)
        page = request.GET.get('page')
        all_tasks= pagiantor.get_page(page)

        return render(request, 'tasklist.html',{'all_tasks':all_tasks})

def home(request):
    context ={
    "welcome_text":""
}
    return render(request, 'index.html',context)

def contact(request):
    context ={
    "welcome_text":"contact"
}
    return render(request, 'contact.html',context)
@login_required
def delete_task(request, task_id):
    
        task = TaskList.objects.get(pk=task_id)
        if task.manage==request.user:
            task.delete()
        else:
          messages.error(request,("Access Denied!"))
        return redirect(tasklist)
@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.status= True
        task.save()
    else:
        messages.error(request,("Access Denied!"))

    return redirect(tasklist)
@login_required
def notcomplete_task(request, task_id):
     task = TaskList.objects.get(pk=task_id)
     task.status= False
     task.save()
     return redirect(tasklist)   
 
@login_required
def edit_task(request,task_id):
    if request.method =="POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None , instance = task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Edited"))
        return redirect(tasklist)
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html',{'task_obj':task_obj})