"""
This file defines inventory-specific models for database management: Warehouse, Product
"""

from django.db import models

class Warehouse(models.Model):
    """
    Represents a warehouse for storing inventory items.
    """
    name= models.CharField(max_length=255, help_text='Name of the warehouse')
    location= models.CharField(max_length=255, help_text='Location of the warehouse')
    capacity= models.IntegerField(help_text='Maximum storage capacity of the warehouse')

    def __str__(self):
        return f'{self.name} | {self.location}'


class Product(models.Model):
    """
    Represents the inventory items in the warehouse
    """
    name= models.CharField(max_length=255, null=False,help_text='Name of the product')
    sku= models.CharField(max_length=100, unique=True, null=False, help_text='Unique Stock Keeping Unit identifier')
    description= models.CharField(max_length=300, null=False, help_text='Product description')
    price= models.DecimalField(max_digits=10, null=False, decimal_places=2, help_text='Product price')
    quantity= models.IntegerField(default=0, help_text='Product stock available in inventory')

    # foreign relationships
    warehouse=models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name='products',
        related_query_name='product',
        help_text='Warehouse housing the product'
    )

    def __str__(self):
        return f'(Product:{self.name}) | (SKU:{self.sku}) | (Warehouse:{self.warehouse})'