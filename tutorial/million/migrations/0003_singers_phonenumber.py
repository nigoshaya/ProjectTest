# Generated by Django 2.2.6 on 2019-10-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('million', '0002_auto_20191016_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='singers',
            name='phoneNumber',
            field=models.CharField(default='', max_length=20),
        ),
    ]