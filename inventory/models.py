from django.db import models

# Create your models here.
CATEGORY = [
    ('NEPLAI_BOOKS', 'NEPLAI_BOOKS'),
    ('INDIAN_BOOKS', 'INDIAN_BOOKS'),
    ('STATIONARY', 'STATIONARY'),
]

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY, default='NEPALI_BOOKS')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
   

