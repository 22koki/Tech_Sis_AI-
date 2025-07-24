from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    UserProfile, Course, Module, Progress,
    ConfidenceLog, Mentor, MentorshipMatch, SessionFeedback
)
from .serializers import *


from .models import StudyMaterial, AgeBasedTip, StructuredContent
from .serializers import StudyMaterialSerializer, AgeBasedTipSerializer, StructuredContentSerializer


# 1. User Profile
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(detail=True, methods=["get"])
    def content_by_age(self, request, pk=None):
        user = self.get_object()
        age = user.age

        if age <= 15:
            content = {
                "games": ["Math Safari", "CodeCraft Jr.", "Health Adventures"],
                "cartoons": ["Girl Tech Heroes", "Anatomy for Kids"],
                "female_tips": "Did you know? Girls start puberty earlier than boys. It's okay to feel different — you're growing strong!",
            }
        elif 15 < age <= 18:
            content = {
                "skills": ["Python Basics", "Intro to Digital Marketing", "Financial Literacy"],
                "career_pathways": ["Web Dev", "AI", "Entrepreneurship"],
                "female_tips": "Track your periods with a simple calendar app. Learn what changes are normal and what needs attention.",
            }
        else:
            content = {
                "ai_support": ["AI mentors available for emotional & skill support"],
                "topics": ["Leadership", "Advanced Tech", "Self-Discovery"],
                "female_tips": "Your body is unique. Embrace your cycle, rest when needed, and nourish with iron-rich foods.",
            }

        return Response(content)

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

    @action(detail=True, methods=["get"])
    def available_mentees(self, request, pk=None):
        mentor = self.get_object()
        matches = MentorshipMatch.objects.filter(mentor=mentor)
        return Response(MentorshipMatchSerializer(matches, many=True).data)

# 7. Mentorship Match
class MentorshipMatchViewSet(viewsets.ModelViewSet):
    queryset = MentorshipMatch.objects.all()
    serializer_class = MentorshipMatchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['learner__user__username', 'mentor__user__username']

# 8. Feedback
class SessionFeedbackViewSet(viewsets.ModelViewSet):
    queryset = SessionFeedback.objects.all()
    serializer_class = SessionFeedbackSerializer
class StudyMaterialViewSet(viewsets.ModelViewSet):
    queryset = StudyMaterial.objects.all()
    serializer_class = StudyMaterialSerializer

class AgeBasedTipViewSet(viewsets.ModelViewSet):
    queryset = AgeBasedTip.objects.all()
    serializer_class = AgeBasedTipSerializer

class StructuredContentViewSet(viewsets.ModelViewSet):
    queryset = StructuredContent.objects.all()
    serializer_class = StructuredContentSerializer