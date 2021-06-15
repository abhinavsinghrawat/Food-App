from django.db import models

# import existing User model
from django.contrib.auth.models	import User

# Create Class for Profile
class Profile(models.Model):
	# to create mapping i.e use User model in your created profile model, we use OneToOneField()
	# here, on_delete refers that profile gets deleted on deletion of User
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	# Field to add image
	# added default value
	# upload_to refers to directory where all pictures are uploaded
	image = models.ImageField(default='profilepic.jpg', upload_to='profiles_pictures')
	location = models.CharField(max_length=100)


	# string representation
	def __str__(self):
		return self.user.username