# Generated by Django 4.2.7 on 2023-11-04 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='killer',
            old_name='about',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='killer',
            old_name='name',
            new_name='title',
        ),
    ]
