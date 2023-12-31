from django.contrib import admin
from django.urls import path
from .views import snack_listView , snack_detailView , SnackCreateView, SnackUpdateView , SnackDeleteView

urlpatterns = [
    path('',snack_listView.as_view(), name='snack_list'),
    path('<int:pk>/',snack_detailView.as_view(), name='snack_detail'),
    path('create/',SnackCreateView.as_view(), name='snack_create'),
    path('<int:pk>/update/',SnackUpdateView.as_view(), name='snack_update'),
    path('<int:pk>/delete/',SnackDeleteView.as_view(), name='snack_delete'),
]