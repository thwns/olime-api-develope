from django.urls import path
from rest_framework import routers

from .views import TrackViewSet, like_track

router = routers.SimpleRouter()
router.register('tracks', TrackViewSet)

urlpatterns = router.urls + [
    path('like/<int:pk>/', like_track, name='like_track')
]