# Generated by Django 4.1 on 2022-11-12 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0009_alter_issuecomment_mentioned_issues_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuecomment',
            name='mentioned_comments',
            field=models.ManyToManyField(blank=True, to='issues.issuecomment'),
        ),
    ]
