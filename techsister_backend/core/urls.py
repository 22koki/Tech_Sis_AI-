from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileViewSet,
    CourseViewSet,
    ModuleViewSet,
    ProgressViewSet,
    ConfidenceLogViewSet,
    MentorViewSet,
    MentorshipMatchViewSet,
    SessionFeedbackViewSet
)

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet, basename='userprofile')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'modules', ModuleViewSet, basename='module')
router.register(r'progress', ProgressViewSet, basename='progress')
router.register(r'confidence-logs', ConfidenceLogViewSet, basename='confidencelog')
router.register(r'mentors', MentorViewSet, basename='mentor')
router.register(r'matches', MentorshipMatchViewSet, basename='match')
router.register(r'session-feedbacks', SessionFeedbackViewSet, basename='sessionfeedback')

urlpatterns = [
    path('', include(router.urls)),

    # Optional: custom endpoints (if not using DRF @action URLs)
    # path('user-profiles/<int:pk>/content/', UserProfileViewSet.as_view({'get': 'content_by_age'})),
    # path('mentors/<int:pk>/mentees/', MentorViewSet.as_view({'get': 'available_mentees'})),
]
