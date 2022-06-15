# Generated by Django 4.0.4 on 2022-05-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0007_remove_waiter_cafe_cafe_waiters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='waiters',
        ),
        migrations.AddField(
            model_name='waiter',
            name='cafe',
            field=models.ManyToManyField(blank=True, to='tips.cafe'),
        ),
    ]
