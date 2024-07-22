from django.contrib import admin
from django.urls import path
from app.views import Login, Logout, SignUp, index, CreateCourse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('create/', CreateCourse.as_view(), name='create'),
    path('', index, name='home')
]
