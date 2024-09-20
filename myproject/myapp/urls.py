from django.urls import path
from .views import BarangView

urlpatterns = [
    path('barang/', BarangView.as_view(), name='barang-list'),
]
