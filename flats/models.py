from django.db import models


class Flat(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    furnished = models.CharField(max_length=50)

    def __str__(self):
        return self.name