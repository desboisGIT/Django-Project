from django.db import models

# Create your models here.
class item(models.Model):

    def __str__(self):
        return self.item_name + ", price: " + str(self.item_price)  + "€"
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()