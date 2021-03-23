from django.urls import path
from commerce.views import ProductListView

app_name = 'commerce'

urlpatterns = [
    path('', ProductListView.as_view(), name = 'productlist')
]