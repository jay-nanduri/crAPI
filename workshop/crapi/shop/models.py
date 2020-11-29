"""
Models related to Shop
Product and Order Models
"""
from django.db import models

from user.models import User


class Product(models.Model):
    """
    Product Model
    represents a product in the application
    """

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return f"{self.name} - {self.price}"


class Order(models.Model):
    """
    Order Model
    represents an order in the application
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_on = models.DateTimeField()

    DELIVERED = "delivered"
    RETURN_PENDING = "return pending"
    RETURNED = "returned"

    STATUS_CHOICES = (
        (DELIVERED, "delivered"),
        (RETURN_PENDING, "return pending"),
        (RETURNED, "returned")
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DELIVERED)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return f"{self.user.email} - {self.product.name} "

class Coupon(models.Model):
    """
    AppliedCoupon Model
    represents a mapping between coupon_code and user
    """
    coupon_code = models.CharField(max_length=255, primary_key=True)
    amount = models.CharField(max_length=255)

    class Meta:
        db_table = 'coupons'
        managed=False

    def __str__(self):
        return f"{self.coupon_code} - {self.amount}"

class AppliedCoupon(models.Model):
    """
    AppliedCoupon Model
    represents a mapping between coupon_code and user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon_code = models.CharField(max_length=255)

    class Meta:
        db_table = 'applied_coupon'

    def __str__(self):
        return f"{self.user.email} - {self.coupon_code} "