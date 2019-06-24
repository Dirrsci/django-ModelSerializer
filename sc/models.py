from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=200, blank=False)

class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    # groups allow blank=True to allow automatic assignemnt if group is not provided
    groups = models.ManyToManyField(Group, blank=True)

    class Meta: 
        ordering = ('name',)