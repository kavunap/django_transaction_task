from django.urls import path
from . import views


urlpatterns = [
    path('', views.orders, name='orders.index'),
	path('create', views.create_order, name='create'),
    # path('detail/<int:school_id>/', views.detail, name='detail'),
    # path('edit/<int:school_id>', views.edit, name='edit'),
    # path('delete/<int:school_id>', views.delete, name='delete'),
]