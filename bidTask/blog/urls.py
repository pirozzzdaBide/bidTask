from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.categories, name='categories'),
    path('new_category/', views.new_category, name='new_category'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/<int:category_id>/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]