from django.db import models

class Client(models.Model):
    name = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 13)

class Address(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    street = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 30)
    zip = models.CharField(max_length = 10)
