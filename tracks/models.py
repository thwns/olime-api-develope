from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile

# Create your models here.
class Track(models.Model):
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracks')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    trackName = models.CharField(max_length=128)
    book = models.CharField(max_length=128)
    subjectMajor = models.CharField(max_length=128)
    subjectSub = models.CharField(max_length=128)
    targetGrade = models.CharField(max_length=128)
    targetTest = models.CharField(max_length=128)
    body = models.TextField()
    imageUrl = models.CharField(max_length=128)
    likes = models.ManyToManyField(User, related_name='like_posts', blank =True)
    feedbacks = models.ManyToManyField(User, related_name='user_feedbacks', blank=True)
    published_date = models.DateTimeField(default=timezone.now)