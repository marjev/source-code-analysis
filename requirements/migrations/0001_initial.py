# Generated by Django 4.2.1 on 2023-06-08 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sourcecodes', '0003_sourcecode_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edges', models.JSONField(verbose_name='Edges')),
                ('nodes', models.JSONField(verbose_name='Nodes')),
                ('source_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sourcecodes.sourcecode')),
            ],
        ),
    ]