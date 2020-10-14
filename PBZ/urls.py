from django.urls import path
from PBZ import views

urlpatterns = [
    path('',views.home_page),
    path('product_page',views.page_product,name='product_page'),
    path('form_product',views.form_product,name='form_product'),
    path('create_product',views.create_product,name='create_product'),
    path('edit_page',views.edit_page,name='edit_page'),
    path('edit/<int:product_id>/',views.edit_product,name='edit_product')

]