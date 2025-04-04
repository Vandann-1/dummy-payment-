from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()  # Price in cents
    image_url = models.URLField()

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_intent_id = models.CharField(max_length=255, unique=True)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"Order {self.id} - {self.status}"
