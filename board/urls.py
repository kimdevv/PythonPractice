from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    path('', post_list),
    path('post/create/', make_post),
    path('post/detail/<int:pk>/', view_post),
    path('post/update/<int:pk>/', edit_post),
    path('post/delete/<int:pk>/', delete_post),
    path('comment/create/<int:pk>/', make_comment),
    path('comment/list/<int:pk>/', view_comment)
]