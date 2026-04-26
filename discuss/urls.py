from django.urls import path

from . import views

app_name = "discuss"

urlpatterns = [
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
]
