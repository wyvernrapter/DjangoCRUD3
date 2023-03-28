from django.urls import path
from .views import ItemFilterView, ItemDetailView

urlpatterns = [
    path('',  ItemFilterView.as_view(), name='Userindex'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
]
