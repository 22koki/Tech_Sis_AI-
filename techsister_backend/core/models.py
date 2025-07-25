from django.db import models
from django.contrib.auth.models import User

# 1. User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    learning_style = models.CharField(max_length=50, choices=[
        ('visual', 'Visual'),
        ('auditory', 'Auditory'),
        ('kinesthetic', 'Kinesthetic'),
    ], null=True, blank=True)
    confidence_score = models.FloatField(default=0.0)
    bio = models.TextField(blank=True, null=True)
    strengths = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    preferred_track = models.CharField(max_length=100, blank=True, null=True)
    is_track_decided = models.BooleanField(default=False)
    language_preference = models.CharField(max_length=20, choices=[
        ('en', 'English'),
        ('sw', 'Swahili'),
        ('fr', 'French'),
        ('ar', 'Arabic'),
    ], default='en')

    def __str__(self):
        return self.user.username


# 2. Educational Content
class EducationalContent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    age_group = models.CharField(max_length=20, choices=[
        ('7-12', '7–12'),
        ('13-15', '13–15'),
        ('16-18', '16–18'),
    ])
    content_type = models.CharField(max_length=30, choices=[
        ('game', 'Game'),
        ('cartoon', 'Cartoon'),
        ('lesson', 'Lesson'),
        ('health_tip', 'Health Tip'),
        ('quiz', 'Quiz'),
    ])
    language = models.CharField(max_length=20, choices=[
        ('en', 'English'),
        ('sw', 'Swahili'),
        ('fr', 'French'),
        ('ar', 'Arabic'),
    ], default='en')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.age_group})"


# 3. Study Material
class StudyMaterial(models.Model):
    content = models.ForeignKey(EducationalContent, related_name='materials', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='materials/videos/', null=True, blank=True)
    notes = models.FileField(upload_to='materials/notes/', null=True, blank=True)
    pdf = models.FileField(upload_to='materials/pdfs/', null=True, blank=True)
    article = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Material for {self.content.title}"


# 4. Courses and Modules
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('coding', 'Coding'),
        ('marketing', 'Digital Marketing'),
        ('entrepreneurship', 'Entrepreneurship'),
        ('soft_skills', 'Soft Skills'),
        ('finance', 'Financial Literacy'),
    ])
    level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.PositiveIntegerField()
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    notes = models.FileField(upload_to='notes/', null=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return f"{self.course.title} - {self.title}"


# 5. Progress Tracking
class Progress(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.module.title}"
class Tip(models.Model):
    age_range = models.CharField(max_length=50)
    tip = models.TextField()

    def __str__(self):
        return f"Tip for age {self.age_range}"


# 6. Confidence Log
class ConfidenceLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reflection_text = models.TextField()
    tone_score = models.FloatField(default=0.0)
    suggestion_given = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d')}"


# 7. Mentorship
class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=100)
    bio = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Mentor: {self.user.username}"


class MentorshipMatch(models.Model):
    learner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    matched_on = models.DateTimeField(auto_now_add=True)
    learning_goal = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.learner.user.username} matched with {self.mentor.user.username}"


class SessionFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True)
    feedback_text = models.TextField()
    was_helpful = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"


# 8. Age-Based Tips and Content
class AgeBasedContent(models.Model):
    title = models.CharField(max_length=255)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    language = models.CharField(max_length=50)
    content_type = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


class AgeBasedTip(models.Model):
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    tip = models.TextField()
    language = models.CharField(max_length=50, default='English')

    def __str__(self):
        return f"Tip for {self.age_min}-{self.age_max}"


class StructuredContent(models.Model):
    age_group = models.CharField(max_length=50)
    category = models.CharField(max_length=100)  # e.g., "Health", "Finance", "Coding"
    language = models.CharField(max_length=50, default='English')
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.age_group}, {self.category})"
