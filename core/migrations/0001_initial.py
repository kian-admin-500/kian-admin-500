# Generated by Django 4.2.4 on 2023-08-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoneAdminTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=20, null=True)),
                ('password', models.TextField(max_length=20, null=True)),
            ],
        ),
    ]