from django.contrib.auth.models import User
from django.db import models

CHOICES = (
    (1, 'fundacja'), (2, 'organizacja pozarządowa'), (3, 'zbiórka lokalna'))
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Insitution(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.IntegerField(choices=CHOICES, default=1, null=True, blank=True)
    category = models.ManyToManyField(Category)

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    insitution = models.ForeignKey(Insitution, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    city = models.TextField()
    zip_code = models.TextField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)