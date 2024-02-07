from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

from .routers import router
from .views.views import UserView

urlpatterns = [
    path('user/', include(router.urls)),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/', UserView.as_view(), name='auth-me'),
]
