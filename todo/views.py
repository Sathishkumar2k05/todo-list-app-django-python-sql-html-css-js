from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.views import View

class TaskListView(View):

    def get(self, request):

        context ={
        "tasks":Task.objects.all()
        } 

        print(request)

        return render(request, 'task_list.html', context)

class TaskAddView(View):

    def get(self,request):

        context = {
            "task_form":TaskForm()
        }

        return render(request, 'task_form.html',context)
    
    def post(self,request):

        task_form = TaskForm(request.POST)

        if task_form.is_valid():

            task_form.save()

        return redirect('task_list')

class TaskUpdateView(View):

    def get(self,request,id):

        selected_task = Task.objects.get(id=id)

        context = {
            "task_form":TaskForm(instance=selected_task)
        }

        return render(request, 'task_form.html',context)
    
    def post(self,request,id):

        selected_task = Task.objects.get(id=id)

        task_form = TaskForm(request.POST, instance=selected_task)

        if task_form.is_valid():

            task_form.save()

        return redirect('task_list')

class TaskDeleteView(View):

    def get(self,request,id):

        context = {
            "selected_task":Task.objects.get(id=id)
        }

        return render(request, 'task_confirm_delete.html', context)
    
    def post(self, request, id):

        selected_task = Task.objects.get(id=id)

        selected_task.delete()
        
        return redirect('task_list')