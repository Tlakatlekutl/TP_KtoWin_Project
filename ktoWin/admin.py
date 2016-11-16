from django.contrib import admin
from .models import Post, Comment, Like
from .models import UserProfile
from .models import Game
from .models import Tag

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(UserProfile)
admin.site.register(Game)
admin.site.register(Tag)
