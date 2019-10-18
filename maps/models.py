from django.db import models

class Client(models.Model):
    name = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 13)
    def __str__(self):
        return self.name

class Address(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    street = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 30)
    zip = models.CharField(max_length = 10)
    longitude = models.CharField(max_length = 200, null=True)
    latitude = models.CharField(max_length = 200, null=True)
    def __str__(self):
        return str(self.street)+", "+str(self.city)+", "+str(self.state)
