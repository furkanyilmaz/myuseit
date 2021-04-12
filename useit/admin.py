from django.contrib import admin

# Register your models here.
from useit.models import Tool, Goodside, Badside

admin.site.register(Tool)
admin.site.register(Goodside)
admin.site.register(Badside)
