from django.forms import forms
from .models import Student

# Import all class or tables present in models.py
from .models import *
from django import forms


# StudentForm is the model form class name
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student  # represents in which table you need to store the information you this form
        fields = "__all__"  # represent models we need to show in frontend
