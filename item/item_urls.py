from django.urls import path
from . import views


urlpatterns = [
    path('', views.items, name='items.index'),
	# path('create', views.create, name='create'),
    # path('detail/<int:school_id>/', views.detail, name='detail'),
    # path('edit/<int:school_id>', views.edit, name='edit'),
    # path('delete/<int:school_id>', views.delete, name='delete'),
]