# Generated by Django 3.2.5 on 2021-07-19 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0003_auto_20210719_1805'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wallet',
            new_name='UserWallet',
        ),
    ]
