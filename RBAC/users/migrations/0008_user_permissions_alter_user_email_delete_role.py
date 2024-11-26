# Generated by Django 5.1 on 2024-11-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='permissions',
            field=models.ManyToManyField(related_name='roles', to='users.permission'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='ex@gmail.com', max_length=254, unique=True),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]