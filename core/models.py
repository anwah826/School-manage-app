from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES =[
        ('student', 'Student'),
        ('admin','Admin')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank= True, null=True)
    student_id = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)


    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
       return self.title
    

class SupportMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)