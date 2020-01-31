from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    displayname = models.CharField(max_length=50)
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

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('user-show', args=[str(self.id)])

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=256)
    author = models.ForeignKey('Profile', on_delete=models.PROTECT, blank=True, null=True)
    likes = models.ManyToManyField('Profile', related_name = 'liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content

class Comment(models.Model):
    content = models.CharField(max_length=256)
    author = models.ForeignKey('Profile', on_delete=models.PROTECT)
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    likes = models.ManyToManyField('Profile', related_name='liked_comments')
    replies = models.ManyToManyField('self')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
