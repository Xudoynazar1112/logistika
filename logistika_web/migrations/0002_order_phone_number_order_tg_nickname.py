# Generated by Django 5.1 on 2024-08-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistika_web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.IntegerField(default=941234567),
        ),
        migrations.AddField(
            model_name='order',
            name='tg_nickname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
