# Generated by Django 3.2.9 on 2022-02-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
