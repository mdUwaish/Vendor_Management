from django.urls import path
from .views import create_vendor, get_vendors,get_vendor_by_id,update_vendor_by_id, delete_vendor_by_id,create_purchase_order,get_purchase_order_all
from .views import get_purchase_order_id_detail,get_purchase_order_update,get_purchase_order_delete,get_vendor_performance
urlpatterns =[
    path('api/vendors/', create_vendor, name='create_vendor'),
    path('get_vendors/', get_vendors, name='get_vendors'),
    path('api/vendors/id/',get_vendor_by_id, name='get_vendor_by_id'),
    path('api/vendors/update/', update_vendor_by_id, name='update_vendor_by_id'),
    path('api/vendors/delete/', delete_vendor_by_id, name='delete_vendor_by_id'),
    path('api/purchase_order/', create_purchase_order, name='create_purchase_order'),
    path('api/purchase_order_all/', get_purchase_order_all, name='get_purchase_order_all'),
    path('api/purchase_order/id/', get_purchase_order_id_detail, name='get_purchase_order_id_detail'),
    path('api/purchase_order/update/', get_purchase_order_update, name='get_purchase_order_update'),
    path('api/purchase_order/delete/', get_purchase_order_delete, name='get_purchase_order_delete'),
    path('api/vendors/performance/', get_vendor_performance, name='get_vendor_performance'),
]