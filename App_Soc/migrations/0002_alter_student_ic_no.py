# Generated by Django 3.2.8 on 2021-11-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Soc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ic_no',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='No. Kad Pengenalan'),
        ),
    ]
