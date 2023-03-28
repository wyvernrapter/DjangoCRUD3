from django.urls import path
from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, SearchClearView
urlpatterns = [
    path('',  ItemFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    path('search_clear/', SearchClearView.as_view(), name='search_clear'),
    path('items/', ItemFilterView.as_view(), name='item_filter'),
]
