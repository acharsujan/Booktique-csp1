# Generated by Django 2.1.7 on 2019-03-10 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190310_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='condn',
            field=models.TextField(blank=True),
        ),
    ]
