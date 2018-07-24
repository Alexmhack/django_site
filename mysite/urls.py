from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/login/', views.login, name='login'),
    path('accounts/login/', views.logout, name='logout', kwargs={'next_page': '/'}),
]