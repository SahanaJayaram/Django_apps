from django import forms
from .models import Person
from .models import Login_details

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person

class LoginForm(forms.ModelForm):
	class Meta:
		model = Login_details
