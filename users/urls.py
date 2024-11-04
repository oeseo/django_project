from django.urls import path
from . import views

urlpatterns = [
    path('users-page/', views.users_list, name='users_list'),
    path('add-user/', views.add_user, name='add_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('add-position/', views.add_position, name='add_position'),
    path('positions/', views.positions_list, name='positions_list'),
    path('delete-position/<int:position_id>/', views.delete_position, name='delete_position'),
]