from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from users.api.views import UserViewSet
from cars.api.views import CarsViewSet, ColorsViewSet


router = DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'cars', CarsViewSet)
router.register(r'colors', ColorsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]