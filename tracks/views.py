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
    filterset_fields = ['leader', 'subjectMajor', 'subjectSub', 'targetGrade','targetTest', 'likes']
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
def like_track(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.user in track.likes.all():
        track.likes.remove(request.user)
    else:
        track.likes.add(request.user)

    return Response({'status': 'ok'})
    