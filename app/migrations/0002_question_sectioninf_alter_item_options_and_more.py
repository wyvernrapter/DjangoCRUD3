# Generated by Django 4.1.4 on 2023-01-29 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [

        migrations.CreateModel(
            name='sectioninf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=200, null=True, verbose_name='部署')),
                ('rank', models.CharField(max_length=200, null=True, verbose_name='役職')),
            ],
        ),

    ]
