from django.core.management.base import BaseCommand
from faker import Faker
from shop.models import Brand, Category


class Command(BaseCommand):
    help = "Generate 10 fake brands and 10 fake categories"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            name = fake.unique.company()
            description = fake.text(max_nb_chars=200)
            brand, created = Brand.objects.get_or_create(
                name=name, defaults={"description": description}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Brand created: {name}"))
            else:
                self.stdout.write(f"Brand already exists: {name}")

        for _ in range(10):
            name = fake.unique.word().capitalize()
            description = fake.text(max_nb_chars=150)
            category, created = Category.objects.get_or_create(
                name=name, defaults={"description": description}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Category created: {name}"))
            else:
                self.stdout.write(f"Category already exists: {name}")

        self.stdout.write(
            self.style.SUCCESS("Finished creating 10 brands and 10 categories")
        )
