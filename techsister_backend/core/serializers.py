from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    UserProfile, Course, Module, Progress,
    ConfidenceLog, Mentor, MentorshipMatch, SessionFeedback
)

# Optional: User serializer if needed for nested data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'

class ConfidenceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfidenceLog
        fields = '__all__'

class MentorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Mentor
        fields = '__all__'

class MentorshipMatchSerializer(serializers.ModelSerializer):
    learner = UserProfileSerializer(read_only=True)
    mentor = MentorSerializer(read_only=True)

    class Meta:
        model = MentorshipMatch
        fields = '__all__'

class SessionFeedbackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    mentor = MentorSerializer(read_only=True)

    class Meta:
        model = SessionFeedback
        fields = '__all__'
