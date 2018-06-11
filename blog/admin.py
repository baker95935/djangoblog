from django.contrib import admin
from blog.models import BlogsPost
from blog.models import Member
from blog.models import Link
from blog.models import PostType

# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'timestamp']

class MemberAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'timestamp']

class LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'order', 'timestamp']

class PostTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'timestamp']

admin.site.register(BlogsPost, BlogsPostAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(PostType, PostTypeAdmin)