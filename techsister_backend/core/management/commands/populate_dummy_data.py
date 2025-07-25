from django.core.management.base import BaseCommand
from core.models import Course, Module, Mentor, StudyMaterial, Tip
import random

class Command(BaseCommand):
    help = "Populates the database with dummy data for testing"

    def handle(self, *args, **kwargs):
        # Clear old data
        Course.objects.all().delete()
        Module.objects.all().delete()
        Mentor.objects.all().delete()
        StudyMaterial.objects.all().delete()
        Tip.objects.all().delete()

        self.stdout.write("🔄 Old data cleared.")

        # Create Courses
        courses = []
        for name in ["Web Dev", "AI Basics", "Financial Literacy"]:
            course = Course.objects.create(
                name=name,
                description=f"This is a beginner-friendly course on {name}."
            )
            courses.append(course)
            self.stdout.write(f"✅ Created course: {name}")

        # Create Modules
        for course in courses:
            for i in range(1, 4):
                Module.objects.create(
                    course=course,
                    title=f"{course.name} Module {i}",
                    content=f"Learning content for {course.name} - part {i}"
                )
            self.stdout.write(f"📚 Modules added to course: {course.name}")

        # Create Mentors
        for name, expertise in [("Aisha M.", "AI"), ("Lilian K.", "Web Dev"), ("Grace T.", "Finance")]:
            Mentor.objects.create(
                name=name,
                expertise=expertise,
                bio=f"Experienced mentor in {expertise}.",
                available=True
            )
            self.stdout.write(f"🧑🏽‍🏫 Mentor created: {name} ({expertise})")

        # Create Study Materials
        for i in range(5):
            StudyMaterial.objects.create(
                title=f"Sample Material {i+1}",
                description="Helpful learning resource.",
                file=None  # You can attach a file manually in admin
            )
        self.stdout.write("📁 Sample study materials created.")

        # Create Tips
        age_groups = ["7-15", "15-18", "18+"]
        for i in range(6):
            Tip.objects.create(
                age_range=random.choice(age_groups),
                tip=f"This is a tip for girls aged {random.choice(age_groups)}. Stay inspired!"
            )
        self.stdout.write("💡 Study tips created.")

        self.stdout.write(self.style.SUCCESS("✅ Dummy data successfully populated!"))
