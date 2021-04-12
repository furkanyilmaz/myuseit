from django.db import models

class Tool (models.Model):

    name = models.CharField(max_length= 50, verbose_name="tool name", blank=True, null= False, unique=True,
                            editable=True)
    content = models.TextField(verbose_name="ürün açıklaması", max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    website = models.URLField(max_length=200)


class Goodside(models.Model):
    content = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

class Badside(models.Model):
    content = models.TextField(verbose_name="ürün yorumu",max_length=500)
    content = models.TextField(max_length=500)


