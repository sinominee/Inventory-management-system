from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('record/<int:pk>', views.product_record, name='record'),
    path('delete/<int:pk>', views.delete_product, name='delete'),
    path('add_product/', views.add_product , name='add_product'),
    path('update_product/<int:pk>', views.update_product , name='update_product'),
]

