import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from users.models import CustomUser as User
from products.models import Product, Category


class Command(BaseCommand):
    help = "Seed the database with initial data (users, categories, products)."

    def handle(self, *args, **kwargs):

        # --- Create Superuser ---
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                phone_number="0700000000",
                password="admin123",
            )
            self.stdout.write(self.style.SUCCESS("Created superuser: admin"))

        # --- Create Normal Users ---
        for i in range(1, 6):
            username = f"user{i}"
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    email=f"user{i}@example.com",
                    phone_number=f"07123456{i:02d}",
                    password="password123",
                    role="user",
                )
                self.stdout.write(self.style.SUCCESS(f"Created user: {username}"))

        # --- Create Categories ---
        category_names = [
            "Electronics", "Clothing", "Books",
            "Home & Kitchen", "Sports", "Garden",
            "Outdoor", "Beauty & Health", "Health & Fitness"]
        categories = []
        for name in category_names:
            category, created = Category.objects.get_or_create(name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created category: {name}"))
            categories.append(category)

        # --- Create Products ---
        product_data = [
            ("Smartphone", "Latest Android smartphone with 6.5-inch display", "Electronics"),
            ("Laptop", "High performance laptop for work and gaming", "Electronics"),
            ("T-shirt", "Comfortable cotton t-shirt", "Clothing"),
            ("Novel", "Bestselling fiction novel", "Books"),
            ("Blender", "Multi-speed kitchen blender", "Home & Kitchen"),
            ("Football", "Standard size 5 football", "Sports"),
            ("Headphones", "Wireless noise-cancelling headphones", "Electronics"),
            ("Sneakers", "Stylish running sneakers", "Clothing"),
            ("Cookbook", "Recipes from around the world", "Books"),
            ("Yoga Mat", "Non-slip yoga mat for fitness", "Sports"),
            ("Garden Tool", "Garden hose with adjustable flow rate", "Home & Kitchen"),
            ("Toothbrush", "Toothbrush with brush head and gentle brushing", "Beauty & Health"),
            ("Fitness Tracker", "Digital fitness tracker for tracking workouts", "Health & Fitness"),
            ("Weight Watcher", "Smart scale for tracking weight and calories", "Health & Fitness"),
            ("Gloves", "Comfortable glove for protecting hands", "Beauty & Health"),
            ("Shower Head", "Adjustable shower head with built-in LED light", "Home & Kitchen"),
            ("Blender Head", "Adjustable blender head with built-in LED light", "Home & Kitchen"),
            ("Shampoo", "Non-greasy shampoo", "Beauty & Health"),
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
                self.stdout.write(self.style.SUCCESS(f"Created product: {name}"))

        self.stdout.write(self.style.SUCCESS("Seeding complete."))
