# Generated by Django 3.2.6 on 2021-08-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='skill_level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
