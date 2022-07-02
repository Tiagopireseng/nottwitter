from django.contrib import admin
from .models import Tweet, Comment, Follow

admin.site.register(Tweet)
admin.site.register(Comment)
admin.site.register(Follow)
