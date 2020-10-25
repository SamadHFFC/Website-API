# Generated by Django 3.1.1 on 2020-10-23 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='team_members',
            field=models.ManyToManyField(through='teams.TeamMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='teammember',
            unique_together={('team', 'user')},
        ),
    ]
