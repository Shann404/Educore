from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, choices=(('student', 'Student'), ('teacher', 'Teacher')))


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)  # Optional video URL
    resource_file = models.FileField(upload_to='resources/', blank=True, null=True)  # Optional file

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

class UserCourse(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)  # Track progress in percentage

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"


class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('Student', 'Student'),
        ('Instructor', 'Instructor'),
        ('Admin', 'Admin'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    email_address = models.EmailField(max_length=255, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    city_or_town = models.CharField(max_length=100, blank=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, blank=True)
    county = models.CharField(max_length=100, blank=True)
    programme = models.CharField(max_length=255, blank=True)
    registration_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    id_number = models.CharField(max_length=50, blank=True)
    is_completed = models.BooleanField(default=False)  # New field to track profile completion


    def __str__(self):
        return self.user.username

