from django.contrib import admin
from django.urls import path
from .views import snack_listView,snack_detailView

urlpatterns = [
    path('',snack_listView.as_view(), name='snack_list'),
    path('<int:pk>/',snack_detailView.as_view(), name='snack_detail')
]