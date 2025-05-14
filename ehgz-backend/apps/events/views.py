from rest_framework import generics, status

from .models import Event, Category
from .pagination import EventPagination
from .serializers import EventSerializer, EventListSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import permissions, filters
from rest_framework.parsers import MultiPartParser


class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    pagination_class = EventPagination
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category__name']
    def post(self, request, *args, **kwargs):
        self.pagination_class = None
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event = serializer.save()
        return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        self.pagination_class = EventPagination

        return super().get(request, *args, **kwargs)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EventSerializer
        return EventListSerializer


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser]
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()
    
    


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()