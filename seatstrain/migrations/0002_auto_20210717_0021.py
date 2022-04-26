# Generated by Django 3.2.5 on 2021-07-16 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatstrain', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seats',
            options={'ordering': ['-NumberOfSeats']},
        ),
        migrations.AlterField(
            model_name='seats',
            name='NumberOfSeats',
            field=models.PositiveIntegerField(default=20),
        ),
    ]