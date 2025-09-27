from django.db import models


class Product(models.Model):
    """
    Product model.

    Attributes:
    name (str): Name of the product.
    description (str): Description of the product.
    categories (ManyToManyField): Categories to which the product belongs.
    price (DecimalField): Price of the product.
    quantity (PositiveIntegerField): Quantity of the product.
    created_at (DateTimeField): Date and time when the product was created.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField(
        'Category',
        related_name='products'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta options for Product model.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        String representation of Product model.
        """
        return self.name


class Category(models.Model):
    """
    Category model.

    Attributes:
    name (str): Name of the category.
    created_at (DateTimeField): Date and time when the category was created.
    """
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of Category model.
        """
        return self.name
