from django.urls import path
from PBZ import views

urlpatterns = [
    path('',views.home_page),
    path('product_page',views.page_product,name='product_page'),
    path('form_product',views.form_product,name='form_product'),
    path('create_product',views.create_product,name='create_product'),
    path('edit_page',views.edit_page,name='edit_page'),
    path('edit/<int:product_id>/',views.edit_product,name='edit_product'),
    path('delete_page',views.delete_page,name='delete_page'),
    path('delete/<int:product_id>/',views.delete_product,name='delete_product'),
    path('show_category',views.show_category_of_product,name='show_category'),
    path('page_waybill',views.page_waybill,name='page_waybill'),
    path('form_waybill',views.form_waybill,name='form_waybill'),
    path('form_customer',views.form_customer,name='form_customer'),
    path('create_customer',views.create_customer,name='create_customer'),
    path('form_destination',views.form_destination,name='form_destination'),
    path('create_destination',views.create_destination,name='create_destination'),
    path('create_waybill',views.create_waybill,name='create_waybill'),
    path('show_customer',views.show_customer,name='show_customer'),
    path('edit_waybill_page',views.edit_waybill_page,name='edit_waybill_page'),
    path('edit_waybill/<int:waybill_id>/',views.edit_waybill,name='edit_waybill'),
    path('delete_waybill_page',views.page_delete_waybill,name='delete_waybill_page'),
    path('delete_waybill/<int:waybill_id>/',views.delete_waybill,name='delete_waybill')


]