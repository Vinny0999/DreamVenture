from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AuthSignUpCompany(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name =      models.CharField(max_length=200)
    last_name  =      models.CharField(max_length=200)
    phone      =      models.IntegerField()
    email      =      models.CharField(max_length=200)
    address    =      models.CharField(max_length=200)
    city       =      models.CharField(max_length=200)
    state      =      models.CharField(max_length=400)
    zipcode    =      models.IntegerField()

class AuthSignUpStudent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name =      models.CharField(max_length=200)
    last_name  =      models.CharField(max_length=200)
    email      =      models.CharField(max_length=200)
    phone      =      models.IntegerField()

class Contact_Us(models.Model):
    name = models.CharField(max_length=250)
    contact_number = models.IntegerField(blank=True, unique=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact"