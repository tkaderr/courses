from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context={
        "course": Course.objects.all()
    }
    return render(request,'courses/index.html', context)

def delete(request, id):
    context={
        "courses":Course.objects.get(id=id)
    }
    return render(request,'courses/delete.html', context)

def process(request):
    Course.objects.create(name=request.POST["name"], description=request.POST["description"])
    return redirect('/')

def destroy(request,id):
    delete1=Course.objects.get(id=id)
    delete1.delete()
    return redirect('/')
