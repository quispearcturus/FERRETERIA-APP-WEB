# Generated by Django 5.1.1 on 2024-09-25 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_profilesteel'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilesteel',
            name='name_origin',
            field=models.CharField(default='Nullmx', max_length=300),
        ),
    ]
