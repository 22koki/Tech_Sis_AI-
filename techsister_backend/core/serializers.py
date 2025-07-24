from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    UserProfile, Course, Module, Progress,
    ConfidenceLog, Mentor, MentorshipMatch,
    SessionFeedback, AgeBasedContent, StudyMaterial
)

# User Serializer (Nested or used on its own)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# UserProfile Serializer with nested User
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


# Course Serializer (basic)
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


# Module Serializer
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


# Progress Serializer
class ProgressSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    module = ModuleSerializer(read_only=True)

    class Meta:
        model = Progress
        fields = '__all__'


# Confidence log (tone tracking)
class ConfidenceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfidenceLog
        fields = '__all__'


# Mentor Serializer
class MentorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Mentor
        fields = '__all__'


# Mentorship match (learner-mentor pairing)
class MentorshipMatchSerializer(serializers.ModelSerializer):
    learner = UserProfileSerializer(read_only=True)
    mentor = MentorSerializer(read_only=True)

    class Meta:
        model = MentorshipMatch
        fields = '__all__'


# Feedback on mentorship session
class SessionFeedbackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    mentor = MentorSerializer(read_only=True)

    class Meta:
        model = SessionFeedback
        fields = '__all__'


# NEW: Study material serializer for uploading documents/videos/etc.
class StudyMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = '__all__'


# NEW: Age-based content logic (health tips, games, etc.)
class AgeBasedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeBasedContent
        fields = '__all__'
