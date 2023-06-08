from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from searchApp.views import LocationViewSet, CarViewSet, CargoViewSet

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'cars', CarViewSet)
router.register(r'cargos', CargoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
