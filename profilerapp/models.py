from django.db import models

class User_Record(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to="profile_pics/", blank=True, null=True, default="profile_pics/default.jpg")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"