# Generated by Django 4.2.1 on 2023-06-06 12:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourcecodes', '0002_sourcecode_vector'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcecode',
            name='location',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[0, 0], size=2),
            preserve_default=False,
        ),
    ]
