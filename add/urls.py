from django.urls import path
from add import views

urlpatterns = [
        path('', views.AddApiView.as_view(), name='add'),
        path('items/',views.CreateItemView.as_view(), name='create-item'),
        path('update-items/', views.UpdateItemView.as_view(), name='update-item'),

]
