from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('',TaskListView.as_view(), name='task_list'),
    path('create/',TaskAddView.as_view(),name='task_create'),
    path('update/<int:id>/',TaskUpdateView.as_view(),name='task_update'),
    path('delete/<int:id>/',TaskDeleteView.as_view(),name='task_delete'),
]