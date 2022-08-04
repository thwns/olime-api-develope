from django.urls import path
from rest_framework import routers

from .views import TrackViewSet, follow_track

router = routers.SimpleRouter()
router.register('tracks', TrackViewSet)

urlpatterns = router.urls + [
    path('follow/<int:pk>/', follow_track, name='follow_tracks'),
]