from rest_framework import routers
from core.tasks.api.views import TaskAPIView

# look for diference between some routers
router = routers.SimpleRouter()
router.register(r'task', TaskAPIView)
urlpatterns = router.urls