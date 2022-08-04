from rest_framework import serializers

from users.serializers import ProfileSerializer
from .models import Track

class TrackSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Track
        fields = ("pk", "profile", "trackName", "body", "imageUrl", "published_date", "subjectMajor",
                  "subjectSub", "targetGrade", "targetTest", "followers", "feedbacks")


class TrackCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ("trackName", "subjectMajor", "subjectSub", 
                    "targetGrade", "targetTest", "body", "imageUrl")