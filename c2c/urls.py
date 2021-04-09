from django.urls import path
from .api import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Crop2Cash API')


urlpatterns = [
    path('', schema_view),
    path('sellers', views.SignUp, name='seller-signup'),
    path('accounts/login', views.LoginView, name='seller-login'),
    path('sellers/<int:sellerId>/items', views.ItemsView.as_view(), name='item-list'),
    path('sellers/<int:sellerId>/items/<str:slug>', views.SingleItemView.as_view(), name='single-item'),
    path('items', views.GetAllItems.as_view(), name='get-all-items'),
    path('items/<str:slug>', views.GetSingleItem.as_view(), name='get-single-item'),
    path('items/<str:slug>/markInterest', views.MarkAsInterested.as_view(), name='mark-interest'),
]