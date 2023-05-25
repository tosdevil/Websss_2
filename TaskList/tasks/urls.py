from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_home, name = 'tasks_home'),
    # path('create', views.create, name = 'create'),
    path('create/', views.create.as_view(), name = "create"),
    path('<int:pk>/update', views.TaskUpdate.as_view(), name="task_update"),
    path('<int:pk>/delete', views.TaskDelete.as_view(), name="task_delete")
]
