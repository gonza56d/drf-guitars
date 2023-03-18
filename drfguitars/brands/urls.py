from django.urls import path

from .views import BrandViewSet, LineViewSet


brands_list = BrandViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

brands_detail = BrandViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

lines_list = LineViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

lines_detail = LineViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', brands_list, name='brands-list'),
    path('<int:pk>/', brands_detail, name='brands-detail'),
    path('<int:brand_id>/lines/', lines_list, name='lines-list'),
    path('<int:brand_id>/lines/<int:pk>', lines_detail, name='lines-list'),
]
