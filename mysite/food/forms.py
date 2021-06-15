
# Import forms package to create form
from django import forms
# We are importing the model table, which we are going to use in the form
from .models import Item

# creating class for form
class ItemForm(forms.ModelForm):

	# Creating Meta class which holds the information about what fields
	# should be present in the form
	class Meta:
		# Setting which model we are using here
		model = Item
		# Specifying fields which we want in the form
		fields = ['item_name', 'item_desc', 'item_price', 'item_image']