from django.shortcuts import render, get_object_or_404
from .models import Course, Module

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def module_detail(request, module_id):
    module = get_object_or_404(Module, pk=module_id)
    return render(request, 'module_detail.html', {'module': module})

def Sign_up(request, Singup_id):
    singup = get_object_or_404(Sign_up, pk = Singup_id)
    return render(request, 'Sign up.html', {'Sign_up': Sign_up} )
