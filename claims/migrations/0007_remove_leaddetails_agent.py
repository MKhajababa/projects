# Generated by Django 3.2.5 on 2021-09-26 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0006_auto_20210926_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaddetails',
            name='agent',
        ),
    ]
