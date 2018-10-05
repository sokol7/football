from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
#from django_comments.models import Comment

class Country(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=40, blank=True)
    # image = models.ImageField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Country, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.title

class NewsPage(models.Model):
    text = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    country = models.ForeignKey(Country)
    pub_date = models.DateTimeField(auto_created=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    image = models.ImageField(default='image field')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewsPage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='profile_images', blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        self.username = self.user.username
        super(UserProfile, self).save(*args, **kwargs)


    def __str__(self):
        return self.user.username


class Comment(models.Model):
    comment_text = models.CharField(max_length=99999)
    pub_date = models.DateTimeField(auto_now=True)
    news_page = models.ForeignKey(NewsPage, default='')
    user= models.ForeignKey(UserProfile, default='')
    father_comment = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.comment_text