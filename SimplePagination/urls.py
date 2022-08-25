from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("api/v1/posts", views.PostViewSet, basename="posts")

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]