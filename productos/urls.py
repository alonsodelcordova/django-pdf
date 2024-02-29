
from django.urls import path
from .views import ProductoApiView, productos_reporte_pdf, ImagenProductoApiView

urlpatterns = [
    path('productos/', ProductoApiView.as_view(), name='productos'),
    path('productos/reporte/pdf/', productos_reporte_pdf, name='productos_reporte_pdf'),
    path('productos/imagen/<int:pk>/', ImagenProductoApiView.as_view(), name='imagen_producto'),
]