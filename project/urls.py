from django.urls import path
from .views import (
	ProjectListView,
	ProjectCreateView,
	ProjectDeleteView
)
from . import views

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-home'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('delete/<slug:project>', ProjectDeleteView.as_view(), name='project-delete'),
]