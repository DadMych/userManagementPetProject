# Generated by Django 3.2.9 on 2021-11-16 01:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('usersCURD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=30, unique=True),
            preserve_default=False,
        ),
    ]