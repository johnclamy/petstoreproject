from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id}-{self.user.username}"
