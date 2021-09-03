from django.db import models

class Products(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to="images/", db_column='Image', blank=True, null=True)


