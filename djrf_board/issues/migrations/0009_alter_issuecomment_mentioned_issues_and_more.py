# Generated by Django 4.1 on 2022-11-12 18:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0008_issuecomment_mentioned_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuecomment',
            name='mentioned_issues',
            field=models.ManyToManyField(blank=True, related_name='mentioned_in', to='issues.issue'),
        ),
        migrations.AlterField(
            model_name='issuecomment',
            name='mentioned_users',
            field=models.ManyToManyField(blank=True, related_name='mentioned_in', to=settings.AUTH_USER_MODEL),
        ),
    ]
