# Generated by Django 5.1.1 on 2024-09-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_texture_alter_polygon_name_polygon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_shape', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Shape',
                'verbose_name_plural': 'Shapes',
            },
        ),
    ]
