# Generated by Django 3.2.5 on 2021-09-26 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0005_alter_agentuser_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentuser',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='leaddetails',
            name='agent',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='claims.agentuser'),
            preserve_default=False,
        ),
    ]
