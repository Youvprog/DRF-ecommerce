from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    address = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_token = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['-created_at',]
    def __str__(self):
        return f'user is {self.user.username} -- first name= {self.first_name}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} --ordered by-- {self.order.first_name} at: {self.order.created_at}'

    