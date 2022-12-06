from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def list_projects(request):
    projects_list = Project.objects.filter(owner=request.user)
    context = {"projects_list": projects_list}
    return render(request, "projects/list.html", context)
