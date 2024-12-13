"""
This file contains logistics-specific models: Order, Shipment
"""

from django.db import models


class Order(models.Model):
    """
    Represents a customer order in the system
    """
    order_id= models.IntegerField(max_length=50, unique=True, null=False, help_text='Unique identifier for individual customer order')
    customer_name= models.CharField(max_length=255, null=False, help_text='Name of the customer')
    customer_email= models.EmailField(max_length=100, blank=True, null=True, help_text='Email of customer')
    customer_address= models.TextField(null=False, help_text='Delivery address for customer')
    created_at= models.DateTimeField(null=False, auto_now_add=True, help_text='Timestamp of order creation')
    status= models.CharField(
        max_length=50,
        choices=[
            ('PENDING', 'Pending'),
            ('SHIPPED', 'Shipped'),
            ('DELIVERED', 'Delivered'),
            ('CANCELLED', 'Cancelled')
        ],
        default='Pending',
        help_text='Current status of the order'
    )

    def __str__(self):
        return f'Order [{self.order_id}] for: Client {self.customer_name}.'


class Shipment(models.Model):
    """
    Represents shipment details for individual processed orders
    """
    shipment_id= models.IntegerField(max_length=50, unique=True, null=False, )
    shipment_date= models.DateTimeField(null=True, blank=True, help_text='Date of order shipment')
    expected_delivery_date= models.DateTimeField(null=True, blank=True, help_text='Expected date of shipment delivery')
    tracking_number= models.CharField(max_length=100, null=True, blank=True, help_text='Unique identifier for shipment tracking')

    order= models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipments', related_query_name='shipment', help_text='Associated order for the shipment')

    def __str__(self):
        return f'Shipment {self.shipment_id} for Order: [{self.order}].'