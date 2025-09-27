import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from users.models import CustomUser as User
from products.models import Product, Category


class Command(BaseCommand):
    """
    Command to seed the database with initial data
    for users, categories, and products.
    """
    help = "Seeds the database with initial data."

    def handle(self, *args, **kwargs):

        # --- Create Superuser ---
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@gmail.com",
                phone_number="0900000000",
                password="admin123",
            )
            self.stdout.write(self.style.SUCCESS("Created superuser: admin"))

        # --- Create Categories ---
        category_names = [
            "Electronics", "Health & Fitness"
            "Home & Kitchen", "Sports",
            "Outdoor", "Beauty & Health"]
        categories = []
        for name in category_names:
            category, created = Category.objects.get_or_create(name=name)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created category: {name}")
                )
            categories.append(category)

        # --- Create Products ---
        product_data = [
            (
                "Smartphone",
                "Latest Android smartphone with 6.5-inch display",
                "Electronics"
            ),
            (
                "Laptop",
                "High performance laptop for work and gaming",
                "Electronics"
            ),
            ("Yoga Mat", "Non-slip yoga mat for fitness", "Sports"),
            ("Blender", "Multi-speed kitchen blender", "Home & Kitchen"),
            ("Shampoo", "Non-greasy shampoo", "Beauty & Health")
        ]

        for name, desc, cat_name in product_data:
            if not Product.objects.filter(name=name).exists():
                product = Product.objects.create(
                    name=name,
                    description=desc,
                    price=Decimal(random.randint(10, 200)),
                    quantity=random.randint(5, 50),
                )
                category = Category.objects.get(name=cat_name)
                product.categories.add(category)
                self.stdout.write(
                    self.style.SUCCESS(f"Created product: {name}")
                )
        
        self.stdout.write(self.style.SUCCESS("Database seeded with initial data"))
