# Generated by Django 3.1.5 on 2021-01-24 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Minigame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=500)),
                ('photo_alt', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=10000)),
            ],
        ),
    ]