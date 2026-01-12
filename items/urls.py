from django.urls import path

from items import views

urlpatterns = [
    path('buy/<int:item_id>/', views.buy_item, name='buy_item'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]
