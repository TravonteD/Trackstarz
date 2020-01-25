# Generated by Django 3.0.2 on 2020-01-17 01:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('displayname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('startdate', models.DateField(default=django.utils.timezone.now)),
                ('coverphoto', models.ImageField(blank=True, upload_to='cover_images/%Y/%m/%d')),
                ('about', models.TextField(blank=True, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('pinterest', models.URLField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, default='profile_images/2019/08/13/New-Trackstarz-App-logo.png', upload_to='profile_images/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('friends', models.ManyToManyField(blank=True, related_name='_user_friends_+', to='main.User')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.User')),
                ('likes', models.ManyToManyField(related_name='liked_posts', to='main.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.User')),
                ('likes', models.ManyToManyField(related_name='liked_comments', to='main.User')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Post')),
                ('replies', models.ManyToManyField(related_name='_comment_replies_+', to='main.Comment')),
            ],
        ),
    ]
