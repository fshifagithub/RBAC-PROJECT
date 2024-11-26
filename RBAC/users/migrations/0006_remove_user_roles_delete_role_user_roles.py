# Generated by Django 5.1 on 2024-11-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_roles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.CharField(default=True, max_length=200),
        ),
    ]