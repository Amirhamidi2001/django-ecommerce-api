from django.test import TestCase
from django.urls import reverse
from .models import Brand, Category, Product


class BrandModelTest(TestCase):
    """
    Test suite for the Brand model.
    """

    def setUp(self):
        self.brand = Brand.objects.create(name="Test Brand")

    def test_brand_creation(self):
        self.assertEqual(self.brand.name, "Test Brand")

    def test_slug_generation(self):
        self.assertEqual(self.brand.slug, "test-brand")

    def test_str_method(self):
        self.assertEqual(str(self.brand), self.brand.name)

    def test_get_absolute_url(self):
        expected_url = reverse(
            "shop:api-v1:brand-detail", kwargs={"slug": self.brand.slug}
        )
        self.assertEqual(self.brand.get_absolute_url(), expected_url)


class CategoryModelTest(TestCase):
    """
    Test suite for the Category model.
    """

    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Test Category")

    def test_slug_generation(self):
        self.assertEqual(self.category.slug, "test-category")

    def test_str_method(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_get_absolute_url(self):
        expected_url = reverse(
            "shop:api-v1:category-detail", kwargs={"slug": self.category.slug}
        )
        self.assertEqual(self.category.get_absolute_url(), expected_url)

    def test_parent_category(self):
        parent = Category.objects.create(name="Parent Category")
        child = Category.objects.create(name="Child Category", parent=parent)
        self.assertEqual(child.parent, parent)
        self.assertIn(child, parent.children.all())


class ProductModelTest(TestCase):
    """
    Test suite for the Product model.
    """

    def setUp(self):
        self.brand = Brand.objects.create(name="Brand A")
        self.category = Category.objects.create(name="Category A")
        self.product = Product.objects.create(
            name="Product A",
            description="Description for product A",
            price=99.99,
            stock=10,
            category=self.category,
            brand=self.brand,
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Product A")
        self.assertEqual(self.product.price, 99.99)
        self.assertEqual(self.product.stock, 10)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.brand, self.brand)
        self.assertTrue(self.product.is_active)

    def test_slug_generation(self):
        self.assertEqual(self.product.slug, "product-a")

    def test_str_method(self):
        self.assertEqual(str(self.product), self.product.name)

    def test_get_absolute_url(self):
        expected_url = reverse(
            "shop:api-v1:product-detail", kwargs={"slug": self.product.slug}
        )
        self.assertEqual(self.product.get_absolute_url(), expected_url)
