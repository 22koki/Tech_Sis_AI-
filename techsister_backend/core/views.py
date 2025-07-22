from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import UserProfile, Course, Module, Progress, ConfidenceLog, Mentor, MentorshipMatch
from .serializers import *

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class ConfidenceLogViewSet(viewsets.ModelViewSet):
    queryset = ConfidenceLog.objects.all()
    serializer_class = ConfidenceLogSerializer

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorshipMatchViewSet(viewsets.ModelViewSet):
    queryset = MentorshipMatch.objects.all()
    serializer_class = MentorshipMatchSerializer
