from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from pdfdjango.utils.util_pdf import generate_pdf_productos
from .reports.diploma import generate_Diploma

class ProductoApiView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        producto_serializer = ProductoSerializer(productos, many=True)
        return Response(producto_serializer.data)

    def post(self, request):
        producto_serializer = ProductoSerializer(data=request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data, status=201)
        return Response(producto_serializer.errors, status=400)

@api_view(['GET'])
def productos_reporte_pdf(request):
    productos = Producto.objects.all()

    pdf_file = generate_pdf_productos(productos)

    response = HttpResponse(bytes(pdf_file), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="productos.pdf"'
    return response


class ImagenProductoApiView(APIView):
    def get(self, request, pk):
        producto = Producto.objects.get(pk=pk)
        if producto.imagen:
            return HttpResponse(producto.imagen, content_type='image/jpeg')
        return Response(status=404, data='{ "error": "Imagen no encontrada"}')
    
    def put(self, request, pk):
        try:

            producto = Producto.objects.get(pk=pk)
            imagen = request.data['imagen']
            if not imagen:
                return Response(status=400, data='{ "error": "Imagen no encontrada"}')
            if(producto.imagen):
                producto.imagen.delete(save=False)
            producto.imagen = imagen
            producto.save()
            producto_serializer = ProductoSerializer(producto)
            return Response(producto_serializer.data, status=200)
        except Producto.DoesNotExist:
            return Response(status=404, data='{ "error": "Producto no encontrado"}')
        

@api_view(['GET'])
def diploma_ejemplo(request):
    pdf_file = generate_Diploma([])
    response = HttpResponse(bytes(pdf_file), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="diploma.pdf"'
    return response
  