from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, CourseViewSet, LessonViewSet,
    ReflectionViewSet, MentorMatchViewSet, ScholarshipViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'reflections', ReflectionViewSet)
router.register(r'matches', MentorMatchViewSet)
router.register(r'scholarships', ScholarshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
