from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import (
    UserProfile, Course, Module, Progress,
    ConfidenceLog, Mentor, MentorshipMatch, SessionFeedback
)
from .serializers import *

# 1. User Profile
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# 2. Course
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# 3. Module
class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

# 4. Progress
class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

# 5. Confidence Logs
class ConfidenceLogViewSet(viewsets.ModelViewSet):
    queryset = ConfidenceLog.objects.all()
    serializer_class = ConfidenceLogSerializer

# 6. Mentor
class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['expertise', 'user__username']

# 7. Mentorship Match
class MentorshipMatchViewSet(viewsets.ModelViewSet):
    queryset = MentorshipMatch.objects.all()
    serializer_class = MentorshipMatchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['learner__user__username', 'mentor__user__username']

# 8. Feedback (NEW)
class SessionFeedbackViewSet(viewsets.ModelViewSet):
    queryset = SessionFeedback.objects.all()
    serializer_class = SessionFeedbackSerializer
