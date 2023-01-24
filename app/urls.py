from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/app', ProjectViewSet, 'app')

urlpatterns = router.urls