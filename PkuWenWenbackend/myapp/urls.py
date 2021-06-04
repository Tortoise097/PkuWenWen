from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('getSchoolIndex',views.getSchoolIndex),
    path('getCourseIndex',views.getCourseIndex),
    path('getQuestionIndex',views.getQuestionIndex),
    path('getAnswerList',views.getAnswerList),
    path('likeAnswer',views.likeAnswer),
    path('dislikeAnswer',views.dislikeAnswer),
    path('addQuestion',views.addQuestion),
    path('addReply',views.addReply),
    path('openSchool', views.openSchool),
    path('openCourse', views.openCourse),
    path('openQuestion', views.openQuestion),
    path('submitQuestion', views.submitQuestion),
]