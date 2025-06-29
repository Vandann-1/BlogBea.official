from django.contrib import admin
from .models import Blog, Profile, Savedblog, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'custom_choices')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at', 'custom_choices')
    ordering = ('-created_at',)
    prepopulated_fields = {'title': ('title',)}

    def has_delete_permission(self, request, obj=None):
        return True  # Allows deleting blog even with related objects
        

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_picture', 'create_at']
    search_fields = ['user__username']


@admin.register(Savedblog)
class SavedblogAdmin(admin.ModelAdmin):
    list_display = ['user', 'blog', 'timestamp']
    search_fields = ['user__username', 'blog__title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'get_blog_title', 'content', 'timestamp']
    search_fields = ['user__username', 'blog__title', 'content']
    list_filter = ['timestamp']

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'User'

    def get_blog_title(self, obj):
        return obj.blog.title
    get_blog_title.short_description = 'Blog'
