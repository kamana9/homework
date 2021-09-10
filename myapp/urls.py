from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete

urlpatterns = [
    path('',TaskList.as_view(), name='tasks'),
    path('detail/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create/',TaskCreate.as_view(),name='edit'),
    path('update/<int:pk>/',TaskUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',TaskDelete.as_view(),name='remove'),
]
