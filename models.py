from django.db import models
# Create your models here.

class Person(models.Model):
	name = models.CharField('name', max_length=200)
	email = models.EmailField('Email',blank=True)

	def __unicode__(self):
		return self.name
		return self.email

class Login_details(models.Model):
	user_name = models.CharField('user_name', max_length=200)
	password= models.CharField('Password',max_length=200)

	def __unicode__(self):
		return self.user_name
		return self.password
