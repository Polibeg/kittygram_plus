# Generated by Django 3.2 on 2023-05-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_auto_20230516_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('Gray', 'Серый'), ('Black', 'Чёрный'), ('White', 'Белый'), ('Ginger', 'Рыжий'), ('Mixed', 'Микс')], max_length=16),
        ),
    ]
