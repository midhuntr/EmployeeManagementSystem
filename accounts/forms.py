from django import forms
from django.contrib.auth.models import User
from .models import Employee

from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



from django import forms
from .models import FormField

class DynamicForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DynamicForm, self).__init__(*args, **kwargs)
        fields = FormField.objects.all()
        for field in fields:
            if field.field_type == 'text':
                self.fields[field.label] = forms.CharField(label=field.label)
            elif field.field_type == 'number':
                self.fields[field.label] = forms.IntegerField(label=field.label)
            elif field.field_type == 'date':
                self.fields[field.label] = forms.DateField(label=field.label, widget=forms.DateInput(attrs={'type': 'date'}))
            elif field.field_type == 'password':
                self.fields[field.label] = forms.CharField(label=field.label, widget=forms.PasswordInput)

from django import forms
from .models import Employee  # Import Employee model

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'date_of_birth', 'gender', 'marital_status', 'address', 'phone_number', 'job_title', 'department']
