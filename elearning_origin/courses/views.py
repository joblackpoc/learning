from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CommentForm
from marketing.models import Signup

# Create your views here.
def index(request):
    if request.method == "POST":
        email=request.POST["email"]
        new_signup= Signup()
        new_signup.email=email
        new_signup.save()
    return render(request, 'index.html')

def courses(request):
    return render(request, 'courses.html')

def english(request):
    course_list = Course.objects.filter(categories__title='English')

    context = {
        'course_list':course_list
    }
    return render(request, 'english.html', context)

def math(request):
    course_list = Course.objects.filter(categories__title='Math')

    context = {
        'course_list':course_list
    }
    return render(request, 'math.html', context)

def course_detail(request, course_id):
    course= get_object_or_404(Course, id=course_id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user= request.user
            form.instance.course = course
            form.save()
            return redirect('course_detail', course_id=course_id)
    context = {
        'course':course,
        'form':form
    }
    return render(request, 'course_detail.html', context)

def contact(request):
    return render(request, 'contact.html')
