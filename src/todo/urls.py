from . import views
from django.urls import path, include

urlpatterns = [
	path('', views.home, name='home'),
	path('delete/<pk>', views.delete, name='delete'),
	path('edit/<pk>', views.edit, name='edit'),
]