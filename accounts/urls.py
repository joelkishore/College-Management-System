from django.urls import path
from .views import *
urlpatterns = [

    path('',home,name='home'),
    path('login/',log_in,name='login'),
    path('logout/',out,name='logout'),
    path('dash/',ad,name='dash'),
    path('create/',create,name='create'),
    path('delete/',delete_user,name='delete'),
    path('delete_user/<int:user_id>/',delete_user,name='delete_user'),
    path('update/',update_user,name='update_users'),
    path('update_user/<int:user_id>/',update_user,name='update_users_with_id'),
    path('add_class/',class_create,name='add_class'),
    path('delete_class/<int:pk>/',delete_class,name='delete_class'),
    path('viewschedule/',viewschedule,name='viewschedule'),
    # path('add_subject/',assign,name='assign'),
]