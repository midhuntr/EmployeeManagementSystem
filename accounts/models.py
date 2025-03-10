from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)  # Adding address field
    gender = models.CharField(max_length=50)  # Adding gender field
    date_of_birth = models.DateField()  # Adding date_of_birth field
    marital_status = models.CharField(max_length=50)  # Adding marital_status field

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Each form belongs to a user
    position = models.PositiveIntegerField(default=0)  # Store field order in the form

    def __str__(self):
        return f"{self.label} ({self.field_type})"


# FormResponse Model - Store responses to the form fields
class FormResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.ForeignKey(FormField, on_delete=models.CASCADE)
    value = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.field.label}: {self.value}"


# DynamicField Model - A more generic version of fields, used to customize forms dynamically
class DynamicField(models.Model):
    label = models.CharField(max_length=100)  # The label for the field
    field_type = models.CharField(max_length=50)  # Type of the field (e.g., 'text', 'number')

    def __str__(self):
        return self.label
