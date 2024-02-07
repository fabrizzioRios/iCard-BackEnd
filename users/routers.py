
from rest_framework.routers import DefaultRouter
from .viewsets.viewsets import UserViewSet


router = DefaultRouter()

router.register(
    "users",
    UserViewSet,
    basename="users-viewsets"
)
