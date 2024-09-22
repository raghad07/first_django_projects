from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    descriptions = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Products :{self.name}\n'
