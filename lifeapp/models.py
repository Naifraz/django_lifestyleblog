from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from lifeStyleblog.utils import unique_slug_generator

# Create your models here.
class author(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    details=models.TextField()
    def __str__(self):
        return self.name.username
class category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class article(models.Model):
    article_author=models.ForeignKey(author,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    introduction = models.TextField(max_length=200)
    body=models.TextField()
    image = models.ImageField(null=True,blank=True,
                              width_field="width_field",
                              height_field="height_field")
    width_field = models.IntegerField(default=100)
    height_field = models.IntegerField(default=100)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    def get_absolute_url(self):
        return "/article/%i/"% self.slug
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=article)
class comment(models.Model):
    post=models.ForeignKey(article,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    post_comment=models.TextField()

    def __str__(self):
        return self.post.title
class Contatct(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.first_name