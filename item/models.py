from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Item(models.Model):
    name = models.CharField(max_length=255)
    total_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.total_quantity}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="orders")
    items = models.ManyToManyField(
        Item,
        through='OrderedList',
        through_fields=('order', 'item'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_total_quantity(self):
        for line_item in self.OrderedList:
            item = Item.objects.get(id= line_item.item_id)
            item.total_quantity += line_item.quantity
            item.save()

class OrderedList(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="ordered_lists")
    item = models.ForeignKey(Item, on_delete=models.CASCADE,related_name="ordered_lists")
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
