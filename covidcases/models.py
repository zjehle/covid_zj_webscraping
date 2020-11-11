from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=1024,unique=True)
    cases = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()

class State(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024,unique=True)
    cases = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()

class County(models.Model):
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024,unique=True)
    cases = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()