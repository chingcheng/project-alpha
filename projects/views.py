from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def list_projects(request):
    projects_list = Project.objects.filter(owner=request.user)
    context = {"projects_list": projects_list}
    return render(request, "projects/list.html", context)

@login_required
def show_project(request, id):
    project_details = get_object_or_404(Project, id=id)
    context = {
        "project_details": project_details
    }
    return render(request, "projects/detail.html", context)
