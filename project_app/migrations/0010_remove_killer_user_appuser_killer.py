# Generated by Django 4.2.7 on 2023-11-04 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0009_alter_killer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='killer',
            name='user',
        ),
        migrations.AddField(
            model_name='appuser',
            name='killer',
            field=models.ManyToManyField(blank=True, related_name='users', to='project_app.killer'),
        ),
    ]
