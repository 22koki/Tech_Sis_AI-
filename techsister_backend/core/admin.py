from django.contrib import admin
from .models import (
    UserProfile, Course, Module, Progress, ConfidenceLog, Mentor,
    MentorshipMatch, SessionFeedback, AgeBasedContent, AgeBasedTip,
    StructuredContent, EducationalContent, StudyMaterial
)

class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'level']
    inlines = [ModuleInline]

class ProgressInline(admin.TabularInline):
    model = Progress
    extra = 0

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'learning_style', 'preferred_track', 'is_track_decided']
    inlines = [ProgressInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'module', 'completed', 'completed_at']

@admin.register(ConfidenceLog)
class ConfidenceLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'tone_score', 'created_at']

class MentorshipMatchInline(admin.TabularInline):
    model = MentorshipMatch
    extra = 0

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ['user', 'expertise', 'available']
    inlines = [MentorshipMatchInline]

@admin.register(MentorshipMatch)
class MentorshipMatchAdmin(admin.ModelAdmin):
    list_display = ['learner', 'mentor', 'matched_on', 'is_active']

@admin.register(SessionFeedback)
class SessionFeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'mentor', 'was_helpful', 'created_at']

@admin.register(AgeBasedContent)
class AgeBasedContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'age_min', 'age_max', 'language', 'content_type']

@admin.register(AgeBasedTip)
class AgeBasedTipAdmin(admin.ModelAdmin):
    list_display = ['tip', 'age_min', 'age_max', 'language']

@admin.register(StructuredContent)
class StructuredContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'age_group', 'language']

@admin.register(EducationalContent)
class EducationalContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'age_group', 'content_type', 'language', 'is_active']

@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
