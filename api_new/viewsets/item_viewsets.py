from rest_framework.permissions import IsAuthenticated

class ItemViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
=======
    queryset = Item.objects.all().order_by('id')  # garante ordem consistente
    serializer_class = ItemSerializer

>>>>>>> feature/viewsets-tests
