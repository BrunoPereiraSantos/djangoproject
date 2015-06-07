from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
	
	class Meta:
		
		model = SignUp
		fields = ['full_name', 'email']

	#for validade any field create a clean_<field> and raise
	#appropriate errors
	def clean_email(self):
		
		email = self.cleaned_data.get('email')
		email_base, provider = email.split('@')

		##HERE put any sort of validation for these field

		if not 'edu' in provider:
			raise forms.ValidationError('Please make sure that you are using a .edu email address')

		return email 

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')

		#write validation code.

		return full_name
