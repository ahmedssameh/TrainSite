# Generated by Django 3.2.5 on 2021-07-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddingTrain', '0004_rename_distnation_train_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='trainimg',
            field=models.ImageField(default='2.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='train',
            name='destination',
            field=models.CharField(choices=[('cairo', 'cairo'), ('Giza', 'Giza'), ('Alexandria', 'Alexandria'), ('Dakahlia', 'Dakahlia'), ('Sharkia', 'Sharkia'), ('Menoufia', 'Menoufia'), ('Qalyubia', 'Qalyubia'), ('Beheira', 'Beheira'), ('Gharbia', 'Gharbia'), ('Port Said', 'Port Said'), ('Damietta', 'Damietta'), ('Ismailia', 'Ismailia'), ('Suez', 'Suez'), (' Kafr El Sheikh', ' Kafr El Sheikh'), ('Fayoum', 'Fayoum'), ('Beni Suef', 'Beni Suef'), ('Matrouh', 'Matrouh'), ('El Alamein ', 'El Alamein '), ('North Sinai', 'North Sinai'), ('Minya', 'Minya'), ('Sinai', 'Sinai'), ('Minya', 'Minya'), ('Assiut', 'Assiut'), ('Sohag', 'Sohag'), ('Qena', 'Qena'), ('Luxor', 'Luxor'), ('Aswan', 'Aswan'), ('Red Sea', 'Red Sea')], max_length=50),
        ),
        migrations.AlterField(
            model_name='train',
            name='source',
            field=models.CharField(choices=[('cairo', 'cairo'), ('Giza', 'Giza'), ('Alexandria', 'Alexandria'), ('Dakahlia', 'Dakahlia'), ('Sharkia', 'Sharkia'), ('Menoufia', 'Menoufia'), ('Qalyubia', 'Qalyubia'), ('Beheira', 'Beheira'), ('Gharbia', 'Gharbia'), ('Port Said', 'Port Said'), ('Damietta', 'Damietta'), ('Ismailia', 'Ismailia'), ('Suez', 'Suez'), (' Kafr El Sheikh', ' Kafr El Sheikh'), ('Fayoum', 'Fayoum'), ('Beni Suef', 'Beni Suef'), ('Matrouh', 'Matrouh'), ('El Alamein ', 'El Alamein '), ('North Sinai', 'North Sinai'), ('Minya', 'Minya'), ('Sinai', 'Sinai'), ('Minya', 'Minya'), ('Assiut', 'Assiut'), ('Sohag', 'Sohag'), ('Qena', 'Qena'), ('Luxor', 'Luxor'), ('Aswan', 'Aswan'), ('Red Sea', 'Red Sea')], max_length=50),
        ),
    ]
