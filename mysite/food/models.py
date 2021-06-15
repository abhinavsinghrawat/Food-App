from django.db import models

class Item(models.Model):

	def __str__(self):
		return self.item_name

	item_name = models.CharField(max_length=200)
	item_desc = models.CharField(max_length=200)
	item_price = models.IntegerField()
	item_image = models.CharField(max_length=500, default="https://s3.amazonaws.com/ODNUploads/5637b7e513fdbplaceholder_food_item_2.png")