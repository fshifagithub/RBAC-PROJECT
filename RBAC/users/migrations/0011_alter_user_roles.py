# Generated by Django 5.1 on 2024-11-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_user_roles_user_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.CharField(default='User', max_length=200),
        ),
    ]