from django.urls import path
from PBZ import views

urlpatterns = [
    path('',views.home_page),
    path('product_page',views.page_product,name='product_page')

]