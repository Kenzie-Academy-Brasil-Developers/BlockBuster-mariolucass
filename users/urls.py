from django.urls import path
from rest_framework_simplejwt import views
from .views import UserView, UserDetailView

urlpatterns = [
    path("login/", views.TokenObtainPairView.as_view()),
    path("login/refresh/", views.TokenRefreshView.as_view()),
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
]
