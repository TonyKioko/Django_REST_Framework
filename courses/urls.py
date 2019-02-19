
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ListCreateCourse.as_view(), name='course_list')
]
