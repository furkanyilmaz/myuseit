from django.db import models
#from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.base_user import BaseUserManager

"""class UserManager(BaseUserManager):
    use_in_migrations = True

    class Meta:
        abstract = True


    def _create_user(self, email, password):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user """


class User(models.Model):
    name = models.CharField(max_length=40, unique=True,blank= True,)




    def __str__(self):
        return self.name

class Tool(models.Model):
    #user = models.ForeignKey(User, on_delete=models.PROTECT, null= True)  # the owner
    name = models.CharField(max_length=50, verbose_name="tool name", blank=True, null=False, unique=True,
                            editable=True)
    content = models.TextField(verbose_name="ürün açıklaması", max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    website = models.URLField(max_length=200)
    users = models.ManyToManyField(User, blank=True)
    # users = models.ManyToManyField(UserManager, blank=True)

    def __str__(self):
        return self.name


class Goodside(models.Model):
    tool = models.ForeignKey(Tool, null=True, on_delete=models.DO_NOTHING)
    content = models.TextField(max_length=500)
    users = models.ManyToManyField(User, blank=True)
    #created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Badside(models.Model):
    tool = models.ForeignKey(Tool, null=True, on_delete=models.DO_NOTHING)
    content = models.TextField(verbose_name="ürün yorumu", max_length=500)
    users = models.ManyToManyField(User, blank=True)
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
