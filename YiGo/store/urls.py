from django.urls import path


from .views import *

urlpatterns = [
    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update-item/', update_item, name='update-item'),
    path('process-order/', processOrder, name='process-order')
]
