from django.urls import path
from commerce.views import ProductListView, ProductDetailView, UserCreateView, login, logout_view, address
app_name = 'commerce'

urlpatterns = [
    path('', ProductListView.as_view(), name = 'productlist'),
    path('<slug:slug>', ProductDetailView.as_view()),
    path('signup/', UserCreateView.as_view(), name = 'signup'),
    path('login/', login, name = 'login'),
    path('logout/', logout_view, name= 'logout'),
    path('address/', address, name = 'address')
]