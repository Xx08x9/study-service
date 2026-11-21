from rest_framework.routers import DefaultRouter

from assignments.views import AssignmentViewSet
from tests.views import TestViewSet
from materials.views import MaterialViewSet

router = DefaultRouter()

router.register('assignments', AssignmentViewSet, basename='assignment')
router.register('tests', TestViewSet, basename='test')
router.register('materials', MaterialViewSet, basename='material')

urlpatterns = router.urls
