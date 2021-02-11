from django.db import models

#Contestant Model. Is used to register contestants and their data
class Contestant(models.Model):
    email = models.CharField(max_length=320, unique=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    rut = models.CharField(max_length=9)

    class Meta:
        app_label = 'lottery'

    def __str__(self):
        return self.name
