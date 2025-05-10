from django.urls import path
from .views import *
urlpatterns=[
    path('',staff,name='staff'),
    path('announcements/',announcements_view,name='announcements'),
    path('delete_announcements/<int:pk>',delete_announcements,name='delete_announcements'),
    path('add_document/',add_document,name='add_document'),
]
