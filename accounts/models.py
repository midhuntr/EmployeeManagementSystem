from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)  
    gender = models.CharField(max_length=50)  
    date_of_birth = models.DateField()  
    marital_status = models.CharField(max_length=50)  

    def __str__(self):
        return self.full_name


class FormField(models.Model):
    FIELD_TYPES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('password', 'Password'),
    ]

    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    position = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return f"{self.label} ({self.field_type})"


class FormResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.ForeignKey(FormField, on_delete=models.CASCADE)
    value = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.field.label}: {self.value}"


class DynamicField(models.Model):
    label = models.CharField(max_length=100)  
    field_type = models.CharField(max_length=50)  
    def __str__(self):
        return self.label
