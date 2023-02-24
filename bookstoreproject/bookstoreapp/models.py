from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_ids = models.CharField(max_length=200)
    product_ids = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField()
    contact_number = models.BigIntegerField(null=True, blank=True)
    total = models.FloatField()
    status = models.BooleanField(default=False, null=True, blank=True)
    ordered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class IncidentReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    organization = models.TextField(null=True, blank=True)
    description = models.TextField()
    upload_photo = models.ImageField(upload_to='IncidentPhoto', null=True, blank=True)
    action = models.BooleanField(null=True, blank=True, default=False)
    reported_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField()
    contactNo = models.PositiveBigIntegerField()
    address = models.TextField()

    def __str__(self):
        return self.user.username

class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    contactNo = models.PositiveBigIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.user.username