from django.shortcuts import render, get_object_or_404, redirect
from tasks.forms import TaskForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form
    }

    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    tasks_list = Task.objects.all()
    context = {
        "tasks_list": tasks_list
    }
    return render(request, "tasks/list.html", context)
