# Generated by Django 4.1.4 on 2023-02-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_manager_addpro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addpro',
            name='id',
        ),
        migrations.AlterField(
            model_name='addpro',
            name='productname',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
