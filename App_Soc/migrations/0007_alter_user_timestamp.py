# Generated by Django 3.2.8 on 2021-11-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Soc', '0006_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
