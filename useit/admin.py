from django.contrib import admin
#from .models import AbstractUser

# Register your models here.
from useit.models import Tool, Goodside, Badside,User

admin.site.register(User)
admin.site.register(Tool)
admin.site.register(Goodside)
admin.site.register(Badside)


