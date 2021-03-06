# Generated by Django 3.2.5 on 2021-07-05 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddingTrain', '0002_train_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='distnation',
            field=models.CharField(choices=[('Cairo', 'Cairo'), ('Alexandria', 'Alexandria'), ('Fayoum', 'Fayoum'), ('Tanta', 'Tanta'), ('Qena', 'Qena')], max_length=50),
        ),
        migrations.AlterField(
            model_name='train',
            name='source',
            field=models.CharField(choices=[('Cairo', 'Cairo'), ('Alexandria', 'Alexandria'), ('Fayoum', 'Fayoum'), ('Tanta', 'Tanta'), ('Qena', 'Qena')], max_length=50),
        ),
    ]
