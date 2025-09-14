from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, CategoryViewSet, ProductViewSet

app_name = "api-v1"

router = DefaultRouter()
router.register("brands", BrandViewSet)
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)
urlpatterns = router.urls
