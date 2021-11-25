from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list , name='products'),
    path('<int:product_id>/', views.product_display , name='product_display'),
    path('add/', views.add_product , name='add_product'),
    path('update/<int:product_id>/', views.update_product , name='update_product'),
]
