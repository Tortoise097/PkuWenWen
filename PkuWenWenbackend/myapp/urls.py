from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('getSchoolIndex',views.getSchoolIndex),
    path('getCourseIndex',views.getCourseIndex),
    path('getQuestionIndex',views.getQuestionIndex),
    path('addQuestion',views.addQuestion),
    path('openSchool', views.openSchool),
    path('openCourse', views.openCourse),
    path('openQuestion', views.openQuestion),
    path('submitQuestion', views.submitQuestion),
]