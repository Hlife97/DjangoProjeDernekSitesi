from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update,name='user_update'),
    path('password/', views.change_password,name='change_password'),
    path('comments/', views.comments,name='comments'),
    path('contents/', views.contents,name='contents'),
    path('addcontent/', views.addcontent,name='addcontent'),
    path('deletecomment/<int:id>', views.deletecomment,name='deletecomment'),
    path('deletecontent/<int:id>', views.deletecontent,name='deletecontent'),
    path('editcontent/<int:id>', views.editcontent,name='editcontent'),
    path('addgaleri/<int:id>', views.addgaleri,name='addgaleri'),
]