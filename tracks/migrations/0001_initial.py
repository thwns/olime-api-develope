# Generated by Django 4.0.6 on 2022-08-04 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackName', models.CharField(max_length=128)),
                ('book', models.CharField(max_length=128)),
                ('subjectMajor', models.CharField(max_length=128)),
                ('subjectSub', models.CharField(max_length=128)),
                ('targetGrade', models.CharField(max_length=128)),
                ('targetTest', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('imageUrl', models.CharField(max_length=128)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('feedbacks', models.ManyToManyField(blank=True, related_name='user_feedbacks', to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(blank=True, related_name='follow_tracks', to=settings.AUTH_USER_MODEL)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
