# Generated by Django 5.1.1 on 2024-09-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('confirm_password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]