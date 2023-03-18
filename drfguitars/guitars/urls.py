from django.urls import path

from .views import GuitarViewSet


guitars_list = GuitarViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

guitars_detail = GuitarViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', guitars_list, name='guitars-list'),
    path('<int:pk>/', guitars_detail, name='guitars-detail'),
]
