# Generated by Django 4.2.5 on 2023-10-28 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='status',
            new_name='amount',
        ),
        migrations.AddField(
            model_name='students',
            name='year',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
