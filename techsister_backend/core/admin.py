from .models import UserProfile, Course, Module, Progress, ConfidenceLog, Mentor, MentorshipMatch
from django.contrib import admin

admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Progress)
admin.site.register(ConfidenceLog)
admin.site.register(Mentor)
admin.site.register(MentorshipMatch)
