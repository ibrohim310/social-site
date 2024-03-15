from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.UserAPIView.as_view()),
    path('user-relation/', views.UserRelationAPIView.as_view()),
    path('chat/', views.UserAPIView.as_view()),
    path('massage/', views.UserAPIView.as_view()),
    path('following/<int:pk>/', views.following),
    path('follower/<int:pk>/', views.follower),
    
    path('posts/', views.PostCRUD.as_view(), name='post-crud'),
    path('posts/filter/<int:author_id>/', views.PostFilter.as_view(), name='post-filter'),
    path('comments/', views.CommentCRUD.as_view(), name='comment-crud'),
    path('likes/', views.LikeCRUD.as_view(), name='like-crud'),
]