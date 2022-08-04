from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import Profile
from .models import Track
from .permissions import CustomReadOnly
from .serializers import TrackSerializer, TrackCreateSerializer

# Create your views here.
class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    permission_classes = [CustomReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['leader', 'subjectMajor', 'subjectSub', 'targetGrade','targetTest', 'followers']
    filter_backends = [filters.SearchFilter]
    search_fields = ['trackName', 'body']

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return TrackSerializer
        return TrackCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(leader=self.request.user, profile=profile)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def follow_track(request, pk):
    track = get_object_or_404(Track, pk=pk)
    profile = get_object_or_404(Profile, user=request.user)
    if request.user in track.followers.all():
        track.followers.remove(request.user)
        profile.followed_tracks.remove(track.pk)
    else:
        track.followers.add(request.user)
        profile.followed_tracks.add(track.pk)

    return Response({'status': 'ok'})
    