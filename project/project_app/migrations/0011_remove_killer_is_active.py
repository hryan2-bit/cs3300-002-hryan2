# Generated by Django 4.2.7 on 2023-11-04 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0010_remove_killer_user_appuser_killer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='killer',
            name='is_active',
        ),
    ]
