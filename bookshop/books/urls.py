from rest_framework.routers import DefaultRouter
from views import BookAPIView


router = DefaultRouter()
router.register(r'books', BookAPIView)
# router.register(r'accounts', AccountViewSet)
# urlpatterns = router.urls