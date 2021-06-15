# This is imported to render template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item

# Import ItemForm from forms.py
from .forms import ItemForm

# Django needs to know from where to load the template, so we need loader
from django.template import loader

def index(request):

	# Retrieve data from the database and display it over the website 
	item_list = Item.objects.all()

	# here loader is used, with path specified, to load template
	# template = loader.get_template('food/index.html')

	# template always needs a context
	# context: We get the data from the database table. Django takes the templare and combine it 
	# with the data from the database and together reders the final output. 


	context = {
		# pass in the data retrieved from the database table
		# use ',' at the end for context to work
		# This means we are pass item_list(Item.objects.all()) as item_list 
		'item_list': item_list,

	}

	# render the template 
	# Instead of using Httpresponse, we can also directly remder the template
	# return HttpResponse(template.render(context, request))

	return render(request, 'food/index.html', context)

def message(request):
	return HttpResponse('<h1> My name is Abhinav </h1>')

# view to display details of the items
def detail(request, item_id):
	item = Item.objects.get(pk = item_id)
	
	# return HttpResponse("This is item no: %s" % item_id)

	context = {
		'item':item,
	}

	return render(request, 'food/detail.html', context)

def create_item(request):

	# Create object of form class
	form = ItemForm(request.POST or None)

	context = {
		'form':form
	}

	# check if data entered in form is valid or not
	if form.is_valid():
		# Save the data entered in form
		form.save()
		# Redirect to index webpage
		return redirect('food:index')

	return render(request, 'food/item-form.html', context)

def update_item(request, id):
	# Get the item to be updated, by passing id
	item = Item.objects.get(id=id)

	# create and use existing form template, and pass item fetched
	form = ItemForm(request.POST or None, instance=item)

	context = {
		'item': item,
		'form': form
	}

	if form.is_valid():
		form.save()
		return redirect('food:index')

	return render(request, 'food/item-form.html', context)


def delete_item(request, id):
	item = Item.objects.get(id=id)

	if request.method == 'POST':
		# to delete item from table
		item.delete()
		return redirect('food:index')

	context={
		'item':item
	}

	return render(request, 'food/item-delete.html', context)