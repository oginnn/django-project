from django.urls import path, re_path
from .views import (
    store,
    cart,
    checkout,
    updateItem,
    processOrder,
    productDetail
)

urlpatterns = [
    re_path('detail/(?P<slugInput>[\w-]+)', productDetail, name='detail'),
    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', updateItem, name='update'),
    path('process_order/', processOrder, name='process_order')
]