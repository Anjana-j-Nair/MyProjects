from django.urls import path
from . import views

app_name='Todoapp'
urlpatterns = [
    path('',views.tk,name='tk'),
    path('delete<int:t_id>/',views.delete,name='delete'),
    path('update<int:id>/',views.update,name='update'),
    path('cbhome/',views.tasklistview.as_view(),name='cbyhome'),
    path('cbdetails/<int:pk>/',views.taskdetailview.as_view(),name='cbdetails'),
    path('cbupdate/<int:pk>/',views.taskupdateview.as_view(),name='cbupdate'),
    path('cbdelete/<int:pk>/',views.taskdeleteviews.as_view(),name='cbdelete')

]