from django.urls import path, include
from blog import views
from .auth_view import CustomAuthToken, RegisterUserView
urlpatterns = [
    path('Post/', views.PostList.as_view()),
    path('Post/<int:module1_id>/', views.PostDetail.as_view()),
    path('Comment/', views.CommentList.as_view()),
    path('Comment/<int:module2_id>/', views.CommentDetail.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('register/', RegisterUserView.as_view(), name='register'),
]