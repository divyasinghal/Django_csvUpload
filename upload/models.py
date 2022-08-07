from django.db import models

class Store (models.Model):
    id  = models.AutoField(auto_created = True,
                  primary_key = True,
                  serialize = False, 
                  verbose_name ='ID')
    storeId = models.IntegerField()
    sku = models.CharField(max_length = 20)
    productName =models.CharField(max_length=200)
    price = models.FloatField()
    date = models.DateField()