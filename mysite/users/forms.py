
# import package from django to create form
from django import forms

#import django default User model. This is a default model
from django.contrib.auth.models import User

# import UserCreationForm, which we will inherit to the register class
from django.contrib.auth.forms	import UserCreationForm

class RegisterForm(UserCreationForm):

	email = forms.EmailField()

	class Meta:
		# specify model
		model = User
		# fields to show
		fields = ['username', 'email', 'password1', 'password2']
