from django.urls import path, include
from . import views
from daenamu_project import daenamuapp

app_name='daenamuapp'
urlpatterns = [
    path('', views.index, name ='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
]

#id가 3인 게시물을 삭제 -> http://localhost:8000/blog/delete/3
#id가 5인 게시물을 수정 -> http://localhost:8000/blog/update/5