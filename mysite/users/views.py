from django.shortcuts import render, redirect

# Import package to show message
from django.contrib import messages

# import RegisterForm class created
from .forms import RegisterForm

# Import decorator
from django.contrib.auth.decorators import login_required


# Import build in form for registration
# from django.contrib.auth.forms import UserCreationForm

# Create a view for register
def register(request):
	# Check if the method is POST
 	# a method is set to POST when user clicks the signup button
 	# before that the method is not POST
	if request.method == 'POST':

		# this is the default form. We comment out and use our new form created including email
		# form = UserCreationForm(request.POST)

		form = RegisterForm(request.POST)

		# Check for form validation
		if form.is_valid():
			# save form data
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"Welcome {username}, your account has been created")
			# redirect to login page once registered
			return redirect('login')

	else:
		form = RegisterForm()

	context = {
		'form': form
	}

	return render(request, 'users/register.html', context)


# View created to access profile page
# In order to restrict access to profile page only to logged in users, we use decorator

@login_required
def profilepage(request):
	return render(request, 'users/profile.html')