from  django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Course
from .forms import CourseForm
from django.contrib.auth.mixins import UserPassesTestMixin

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home')
    
class Logout(LogoutView):
    next_page = reverse_lazy('login')
    
class CreateCourse(UserPassesTestMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'create_course.html'
    success_url = reverse_lazy('home')
    
    def test_func(self):
        return self.request.user.groups.filter(name='Teachers').exists()