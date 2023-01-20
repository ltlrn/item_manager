from django.urls import path, re_path

from . import views
from .api import DiseaseView

app_name = 'diseases'

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r"^disease/$", DiseaseView.as_view({"post": "create", "get": "list"})),
    path("disease/<int:pk>", DiseaseView.as_view({"delete": "destroy", "get": "retrieve"})),

]
