# Generated by Django 3.2.5 on 2021-07-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WalletId', models.PositiveIntegerField()),
                ('Balance', models.PositiveIntegerField()),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
