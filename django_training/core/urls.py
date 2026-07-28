from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('hello/<str:name>/', views.hello, name='hello'),
    path('items/', views.ItemListView.as_view(), name='item-list'),
    path('items/<int:id>/', views.ItemDetailView.as_view(), name='item-detail'),
]
