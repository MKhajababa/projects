# Generated by Django 3.2.5 on 2021-09-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0004_auto_20210924_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentuser',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
