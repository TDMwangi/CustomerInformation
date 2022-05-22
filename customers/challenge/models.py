from django.db import models

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER, default='Male')
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default=None)
    lat = models.FloatField(blank=True, null=True, )
    lng = models.FloatField(blank=True, null=True)