from django.db import models

# Create your models here.


class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    Category = models.CharField(max_length=50, null=False, blank=False)
    ProductTitle = models.CharField(max_length=50, null=False, blank=False)
    ImageURL = models.CharField(max_length=255, null=False, blank=False)
    Description = models.TextField()

    def __str__(self):
        return self.ProductTitle
