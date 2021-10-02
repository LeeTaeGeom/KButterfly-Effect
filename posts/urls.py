from django.urls import path
from .views import *


app_name = 'posts'
urlpatterns = [
   
    path("postlist/",postlist, name="postlist"),
    path('new_post/',new_post,name="new_post"),
    path('create/',create,name="create"),
    path('detail/<int:id>',detail,name="detail"),
    path('edit_post/<int:id>',edit_post,name="edit_post"),
    path('update/<int:id>',update,name="update"),
    path('delete/<int:id>',delete,name="delete"),
    path('like_toggle/<int:post_id>/',like_toggle, name="like_toggle"),

]