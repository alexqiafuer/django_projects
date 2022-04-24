from django.urls import path

from .views import TaskDetail, TaskList, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<str:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<str:pk>', TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<str:pk>', TaskDelete.as_view(), name="task-delete"),
]