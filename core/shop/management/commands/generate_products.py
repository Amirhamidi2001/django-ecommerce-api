from django.core.management.base import BaseCommand
from faker import Faker
import random

from shop.models import Product, Brand, Category


class Command(BaseCommand):
    help = "Generate 100 fake products"

    def handle(self, *args, **kwargs):
        fake = Faker()

        brands = list(Brand.objects.all())
        categories = list(Category.objects.all())

        if not brands:
            self.stdout.write(
                self.style.ERROR("No brands found. Please create some brands first.")
            )
            return
        if not categories:
            self.stdout.write(
                self.style.ERROR(
                    "No categories found. Please create some categories first."
                )
            )
            return

        for _ in range(100):
            name = fake.unique.catch_phrase()
            description = fake.text(max_nb_chars=200)
            price = round(random.uniform(10.0, 1000.0), 2)
            stock = random.randint(1, 100)
            brand = random.choice(brands)
            category = random.choice(categories)

            product = Product(
                name=name,
                description=description,
                price=price,
                stock=stock,
                brand=brand,
                category=category,
                is_active=True,
            )
            product.save()

        self.stdout.write(self.style.SUCCESS("Successfully created 100 fake products"))
