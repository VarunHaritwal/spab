from django.db import models

# Create your models here.
class SignUp(models.Model):
	full_name = models.CharField(max_length=120)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)

	def __str__(self):
		return self.email