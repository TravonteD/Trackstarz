# Generated by Django 2.2.3 on 2019-08-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190812_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burst',
            name='overview',
            field=models.TextField(blank=True, null=True),
        ),
    ]
