from django.contrib import admin
from .models import Blog , Profile , Savedblog , Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'custom_choices')  # Customize admin list display
    search_fields = ('title', 'user__username')  # Enable search by title and username
    list_filter = ('created_at', 'custom_choices')  # Add filter options
    ordering = ('-created_at',)  # Show latest blogs first
    prepopulated_fields = {'title': ('title',)}  # Auto-generate slug (optional)
  
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
    list_display = ['user', 'blog', 'content', 'timestamp']
    search_fields = ['user__username', 'blog__title', 'content']
    list_filter = ['timestamp']



    
    

