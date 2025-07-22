from rest_framework import serializers
from .models import UserProfile, Course, Module, Progress, ConfidenceLog, Mentor, MentorshipMatch

class UserProfileSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Mentor
        fields = '__all__'

class MentorshipMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorshipMatch
        fields = '__all__'
