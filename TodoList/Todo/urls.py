
from django.contrib import admin
from django.urls import path, include
from Todo import views

urlpatterns = [
    path('', views.index, name='Todo'),
    path('tasks', views.tasks, name='tasks'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('searchdata',views.searchdata,name='searchdata'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
]

