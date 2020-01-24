from django.urls import path
from add import views

urlpatterns = [
        path('', views.AddApiView.as_view(), name='add'),
        path('items/',views.CreateItemView.as_view(), name='create-item'),
        path('item-details/', views.GetItemDetails.as_view(), name='item-details'),
        path('item-update/', views.UpdateItemView.as_view(), name='item-update'),

]
