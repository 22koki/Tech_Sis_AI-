from rest_framework import viewsets
from .models import User, Course, Lesson, Reflection, MentorMatch, ScholarshipOpportunity
from .serializers import (
    UserSerializer, CourseSerializer, LessonSerializer,
    ReflectionSerializer, MentorMatchSerializer, ScholarshipSerializer
)
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class ReflectionViewSet(viewsets.ModelViewSet):
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer

class MentorMatchViewSet(viewsets.ModelViewSet):
    queryset = MentorMatch.objects.all()
    serializer_class = MentorMatchSerializer

class ScholarshipViewSet(viewsets.ModelViewSet):
    queryset = ScholarshipOpportunity.objects.all()
    serializer_class = ScholarshipSerializer
