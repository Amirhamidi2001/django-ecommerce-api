from rest_framework import serializers
from shop.models import Brand, Category, Product


class BrandSerializer(serializers.ModelSerializer):
    """
    Serializer for the Brand model with an absolute URL field.
    """

    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = [
            "id",
            "name",
            "slug",
            "image",
            "description",
            "created_at",
            "updated_at",
            "absolute_url",
        ]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        relative_url = obj.get_absolute_url()
        if request:
            return request.build_absolute_uri(relative_url)
        return relative_url


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model, including children and absolute URL fields.
    """

    children = serializers.SerializerMethodField()
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "parent",
            "children",
            "created_at",
            "updated_at",
            "absolute_url",
        ]

    def get_children(self, obj):
        children = obj.children.all()
        return [child.id for child in children]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        relative_url = obj.get_absolute_url()
        if request:
            return request.build_absolute_uri(relative_url)
        return relative_url


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model with category
    and brand relations and an absolute URL.
    """

    category = serializers.PrimaryKeyRelatedField(read_only=True)
    brand = serializers.PrimaryKeyRelatedField(read_only=True, allow_null=True)

    absolute_url = serializers.SerializerMethodField()

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )
    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(),
        source="brand",
        write_only=True,
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "price",
            "stock",
            "is_active",
            "image",
            "category",
            "brand",
            "category_id",
            "brand_id",
            "created_at",
            "updated_at",
            "absolute_url",
        ]
        read_only_fields = ["slug", "created_at", "updated_at"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        relative_url = obj.get_absolute_url()
        if request:
            return request.build_absolute_uri(relative_url)
        return relative_url
