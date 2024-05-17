from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apis.views.v1 import school, classroom, teacher, student


router = DefaultRouter()

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls)),
    path('', school.index, name='index'),
    path('add/', school.add, name="add"),
    path('add/addSchool/', school.addSchool, name="addSchool"),

    path('school/', school.SchoolListAPIView.as_view()),
    path('school/<int:pk>', school.SchoolAPIView.as_view()),

    path('classroom/', classroom.ClassRoomListAPIView.as_view()),
    path('classroom/<int:pk>', classroom.ClassRoomAPIView.as_view()),

    path('teacher/', teacher.TeacherListAPIView.as_view()),
    path('teacher/<int:pk>', teacher.TeacherAPIView.as_view()),

    path('student/', student.StudentListAPIView.as_view()),
    path('student/<int:pk>', student.StudentAPIView.as_view()),
]
