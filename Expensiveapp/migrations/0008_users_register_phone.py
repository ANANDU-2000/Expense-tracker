# Generated by Django 5.0.6 on 2024-10-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expensiveapp', '0007_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_register',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
