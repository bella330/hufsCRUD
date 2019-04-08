from django.contrib import admin
from django.urls import path
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/빈칸', blogapp.views.detail, name='detail'),
    path('blog/new/', blogapp.views.new, name='new'),
    path('blog/create/', blogapp.views.create, name='create'),
    path('blog/delete/빈칸/', blogapp.views.delete, name='delete'),
    path('blog/update/빈칸/', blogapp.views.update, name='update'),
    path('blog/edit/빈칸/', blogapp.views.edit, name='edit'),

    
]
