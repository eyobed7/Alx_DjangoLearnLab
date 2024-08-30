from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CohortViewSet  # Ensure this import is correct

router = DefaultRouter()
router.register(r'cohort', CohortViewSet, basename='cohort')

urlpatterns = router.urls
