# Generated by Django 3.1.1 on 2020-10-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201004_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subscription',
            field=models.CharField(choices=[('GD', 'Gadget'), ('PL', 'Political')], max_length=200),
        ),
    ]