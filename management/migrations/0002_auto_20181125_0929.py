# Generated by Django 2.1.3 on 2018-11-25 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='total_books_due',
            field=models.IntegerField(default=0),
        ),
    ]
