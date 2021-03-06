# Generated by Django 2.1.3 on 2018-12-04 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_auto_20181203_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=100)),
                ('rating', models.CharField(choices=[('0', '0'), ('.5', '.5'), ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5', '5')], default='2', max_length=2)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Student')),
            ],
        ),
    ]
