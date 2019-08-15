# Generated by Django 2.2.3 on 2019-07-18 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0003_auto_20190711_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Official Yearly', 'yrl'), ('Official Monthly', 'mon'), ('Universe', 'uni')], default='Universe', max_length=30),
        ),
    ]
