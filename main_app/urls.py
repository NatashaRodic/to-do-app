from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('<int:task_id>', views.details, name='details'),
    path('<int:task_id>/update', views.update, name='update'),
    path('<int:task_id>/delete', views.delete, name='delete')
]