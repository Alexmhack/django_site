from django.urls import path

from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/detail/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('post/drafts/', views.post_draft_list, name='post_draft_list'),
]