from django.urls import path
from blogapp.views import *




urlpatterns = [
    
path('add-blog',addblog, name='addblog'),
path('blogs/<int:bg_id>/',viewBg, name="seeblog"),
path('my-blog',myblog,name="myblog"),
path('edit_blog/<int:bg_id>/',edit_blog,name="edit_blog"),
path('delete_blog/<int:bg_id>/',delete_blog,name="delete_blog"),
path("re/<int:blog_id>/",is_reccuring, name="re"),
path("profile",Userprofile,name="profile"),
path("editprofile",editpf,name="editprofile"),
path('blog/<int:blog_id>/comment/', add_comment, name='add_comment'),
path('blog/<int:blog_id>/like/', like_blog, name='like_blog'),
path('save-blog/<int:blog_id>/', savedblog, name="save-blog"),
path('saved-blogs/', saved_blogs_view, name='saved_blogs'),
path('remove-saved-blog/<int:blog_id>/',remove_saved_blog, name='remove_saved_blog'),
path('generate-title/', generate_title, name='generate_title'),
path('generate-description/',generate_description, name='generate_description'),
]


