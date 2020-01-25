from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=50)
    displayname = models.CharField(max_length=50)
    email = models.EmailField()
    # TODO: Figure out what the start field is for
    startdate = models.DateField(default = timezone.now)
    coverphoto = models.ImageField(
            upload_to='cover_images/%Y/%m/%d',
            blank=True
            )
    about = models.TextField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    youtube = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    pinterest = models.URLField(blank=True)
    website = models.URLField(blank = True)
    picture = models.ImageField(
            upload_to='profile_images/%Y/%m/%d', 
            blank=True, 
            default='profile_images/2019/08/13/New-Trackstarz-App-logo.png'
            )
    friends = models.ManyToManyField('self', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.displayname

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=256)
    author = models.ForeignKey('User', on_delete=models.PROTECT, blank=True, null=True)
    likes = models.ManyToManyField('User', related_name = 'liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content

class Comment(models.Model):
    content = models.CharField(max_length=256)
    author = models.ForeignKey('User', on_delete=models.PROTECT)
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    likes = models.ManyToManyField('User', related_name='liked_comments')
    replies = models.ManyToManyField('self')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
