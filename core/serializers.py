from rest_framework import serializers
from .models import User, Course, Lesson, Reflection, MentorMatch, ScholarshipOpportunity
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'role', 'confidence_score', 'learning_style']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class ReflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reflection
        fields = '__all__'

class MentorMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorMatch
        fields = '__all__'

class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipOpportunity
        fields = '__all__'
