# Generated by Django 4.1 on 2022-11-30 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0001_initial'),
        ('spaces', '0006_rename_roles_spacemember_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='org',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spaces', to='orgs.org'),
        ),
    ]
