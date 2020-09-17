from django.urls import path

from .views import *
urlpatterns = [
    path('team/', TeamView.as_view()),
    path('', ImagesView.as_view()),
    path('image/<int:pk>/', ImageView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()),
    path('image/like/', LikeUpdateView.as_view())
]
