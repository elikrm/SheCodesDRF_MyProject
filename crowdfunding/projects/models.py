from django.db import models
from django.contrib.auth import get_user_model

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from datetime import datetime, timedelta 



# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField(default = True)
    date_created = models.DateTimeField(default = datetime.now())
    date_end = models.DateTimeField(default = datetime.now() + timedelta(days = 30))
    # owner = models.CharField(max_length=200)
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='owner_projects')

    def __str__(self):
        return self.title

# @receiver(post_delete, sender=Project)
# def submission_delete(sender, instance, **kwargs):
# 	instance.image.delete(False)

# def pre_save_blog_post_receiever(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = slugify(instance.owner.username + "-" + instance.title)

# pre_save.connect(pre_save_blog_post_receiever, sender=Project)

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
    'Project',
    on_delete=models.CASCADE,
    related_name='pledges'
    )
    # supporter = models.CharField(max_length=200)
    supporter = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='supporter_pledges'
    )