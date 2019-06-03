from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.name, self.description)
