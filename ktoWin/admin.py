from django.contrib import admin
from .models import Post, Comment, Like
from .models import UserProfile
from .models import Game
from .models import Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    readonly_fields = ('like_count', 'commemt_count')
    list_display = ('title', 'like_count', 'created_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(UserProfile)
admin.site.register(Game)
admin.site.register(Tag)
