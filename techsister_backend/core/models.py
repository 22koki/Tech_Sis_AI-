from django.db import models
from django.contrib.auth.models import User

# 1. UserProfile extends the default Django User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    learning_style = models.CharField(max_length=50, choices=[
        ('visual', 'Visual'),
        ('auditory', 'Auditory'),
        ('kinesthetic', 'Kinesthetic'),
    ])
    confidence_score = models.FloatField(default=0.0)  # For tracking AI nudges
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# 2. Course model
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('coding', 'Coding'),
        ('marketing', 'Digital Marketing'),
        ('entrepreneurship', 'Entrepreneurship'),
        ('soft_skills', 'Soft Skills'),
    ])
    level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])

    def __str__(self):
        return self.title

# 3. Module model
class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"
# 4. Progress tracking per module
class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.module.title}"

# 5. ConfidenceLog for AI-based reflection tracking
class ConfidenceLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reflection_text = models.TextField()
    tone_score = models.FloatField(default=0.0)  # AI-sentiment score (e.g., -1 to 1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d')}"

# 6. Mentor profile
class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=100)
    bio = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Mentor: {self.user.username}"

# 7. MentorshipMatch model
class MentorshipMatch(models.Model):
    learner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    matched_on = models.DateTimeField(auto_now_add=True)
    learning_goal = models.TextField()

    def __str__(self):
        return f"{self.learner.user.username} matched with {self.mentor.user.username}"