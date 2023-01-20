from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from . import views
from .views import TaskViewSet

app_name = "bot_api"

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    re_path("", include(router.urls)),
]
