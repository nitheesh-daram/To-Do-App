from django.db import models
from django import forms
import datetime
# Create your models here.

# class ConvertingDateTimeField(models.DateTimeField):
#     def get_prep_value(self, value):
#         return str(datetime.strptime(value, "%Y-%m-%dT%H:%M:%S+0000"))

class item(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.TextField()
    due_date=models.DateTimeField()

class create_form(forms.ModelForm):
    #  due_date=forms.DateTimeField(input_formats=('%Y-%m-%dT%H:%M:%S+0000',),widget=forms.TextInput(attrs={'type':'datetime-local','step':'1'}))
     class Meta:
        model=item
        fields=[
            "name",
            "description",
            "due_date"
        ]

