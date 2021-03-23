from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 128)
    price = models.IntegerField()
    about = models.TextField()
    stock = models.BooleanField(default = True)

    def __str__(self):
        return self.name

