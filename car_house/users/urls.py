from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name="register"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.user_profile, name="profile"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('buy_car/<int:car_id>/', views.buy_car, name='buy_car'),
    path('change_password/', views.UpdatePassword.as_view(), name="change_password"),
]