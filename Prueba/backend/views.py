from tablib import Dataset
from resources import ProductResource
from django.shortcuts import render
#API
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializers
from django.shortcuts import get_object_or_404


def simple_upload(request):
    if request.method == 'POST':
        product_resource = ProductResource()
        dataset = Dataset()
        new_products = request.FILES['myfile']

        imported_data = dataset.load(new_products.read())
        result = product_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            product_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

class ProductoList(generics.ListCreateAPIView):
        queryset = Producto.objects.all()
        serializer_class = ProductoSerializers

        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj