from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'progress', ProgressViewSet)
router.register(r'confidence-logs', ConfidenceLogViewSet)
router.register(r'mentors', MentorViewSet)
router.register(r'matches', MentorshipMatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
