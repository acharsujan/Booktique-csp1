# Generated by Django 2.1.7 on 2019-03-23 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_condn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
