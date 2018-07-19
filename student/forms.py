from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField
class SearchForm(forms.Form):
	erp = forms.CharField(
		label='ERP NO.',
		max_length=50,
	)
	roll = forms.CharField(
		label='Roll NO.',
		max_length=50,
	)

	class Meta:
		model = User
		fields = ('erp','roll', )
		widgets = {
			'erp': forms.TextInput(),
			'roll': forms.TextInput(),
		}

class TeachForm(forms.Form):
	teach = forms.CharField(
		label='Teacher name',
		max_length=50,
	)
	passw = forms.CharField(
		label='Password',
		max_length=50,
	)

	class Meta:
		model = User
		fields = ('teach','passw', )
		widgets = {
			'teach': forms.TextInput(),
			'passw': forms.TextInput(),
		}