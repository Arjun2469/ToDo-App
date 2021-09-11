from django.shortcuts import render, HttpResponse
from Todo.models import Task
# Create your views here.
def index(request):
    context={'success': False}
    if request.method=="POST":
        title =request.POST['title']
        descr =request.POST['descr']
        ins=Task(taskTitle=title, taskDesc=descr)
        ins.save()
        context={'success': True}
    return render(request, 'index.html',context)
def tasks(request):
    allTasks=Task.objects.all()
    context={'tasks': allTasks.order_by('-time')}
    return render(request, 'tasks.html',context)
def delete(request,id):
    obj = Task.objects.get(id=id)
    obj.delete()
    allTasks=Task.objects.all()
    context={'tasks': allTasks.order_by('-time')}
    return render(request, 'tasks.html',context)
def searchdata(request):
    q = request.GET['query']
    allTasks=Task.objects.all()
    context={'tasks': allTasks.filter(taskTitle__contains=q)}
    return render(request,'tasks.html',context)
def edit(request,id):
    obj = Task.objects.get(id=id)
    context = {
        "title" : obj.taskTitle,
        "descr" : obj.taskDesc,
        "id" : obj.id
    }
    return render(request,'edit.html',context)
def update(request,id):
    obj = Task(id=id)
    obj.taskTitle = request.GET['title']
    obj.taskDesc = request.GET['descr']
    import datetime
    updated_at = datetime.datetime.now()
    obj.time = updated_at
    obj.save()
    context = {
        "tasks" : Task.objects.all()
    }
    return render(request,'tasks.html',context)

        