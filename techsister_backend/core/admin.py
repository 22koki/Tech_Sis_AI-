from django.contrib import admin
from .models import (
    UserProfile,
    Course,
    Module,
    Progress,
    ConfidenceLog,
    Mentor,
    MentorshipMatch,
    SessionFeedback,
    AgeBasedContent
)


# Inline: Modules shown inside Course admin
class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'level']
    search_fields = ['title', 'category']
    list_filter = ['category', 'level']
    inlines = [ModuleInline]


# Inline: Progress shown inside UserProfile admin
class ProgressInline(admin.TabularInline):
    model = Progress
    extra = 0


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'learning_style', 'preferred_track', 'is_track_decided']
    search_fields = ['user__username', 'preferred_track']
    list_filter = ['learning_style', 'is_track_decided']
    inlines = [ProgressInline]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']
    search_fields = ['title', 'course__title']
    list_filter = ['course']


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'module', 'completed', 'completed_at']
    search_fields = ['user__username', 'module__title']
    list_filter = ['completed']


@admin.register(ConfidenceLog)
class ConfidenceLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'tone_score', 'created_at']
    search_fields = ['user__username']
    list_filter = ['created_at']


# Inline: Show mentorship matches inside mentor profile
class MentorshipMatchInline(admin.TabularInline):
    model = MentorshipMatch
    extra = 0


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ['user', 'expertise', 'available']
    search_fields = ['user__username', 'expertise']
    list_filter = ['available']
    inlines = [MentorshipMatchInline]


@admin.register(MentorshipMatch)
class MentorshipMatchAdmin(admin.ModelAdmin):
    list_display = ['learner', 'mentor', 'matched_on', 'is_active']
    search_fields = ['learner__user__username', 'mentor__user__username']
    list_filter = ['is_active']


@admin.register(SessionFeedback)
class SessionFeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'mentor', 'was_helpful', 'created_at']
    search_fields = ['user__username', 'mentor__user__username']
    list_filter = ['was_helpful', 'created_at']


@admin.register(AgeBasedContent)
class AgeBasedContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'age_min', 'age_max', 'language', 'content_type']
    search_fields = ['title']
    list_filter = ['content_type', 'language', 'age_min', 'age_max']
