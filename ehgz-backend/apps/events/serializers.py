from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Event, Category, Tag


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']

class EventSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    booked = SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'name_ar',
            'description',
            'description_ar',
            'category',
            'date',
            'venue',
            'price',
            'image',
            'tags',
            'booked'
        ]
        read_only_fields = ['id', 'booked']

    def get_booked(self, obj):
        object = Event.objects.get(id=obj.id)
        """Check if the user is in the booked_by field."""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return object.booked_by.filter(id=request.user.id).exists()
        return False
class EventListSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    booked = SerializerMethodField()
    isAdmin = SerializerMethodField()
    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'name_ar',
            'category',
            'date',
            'venue',
            'price',
            'image',
            'booked',
            'isAdmin'
        ]
        read_only_fields = ['id', 'booked']

    def get_booked(self, obj):
        object = Event.objects.get(id=obj.id)
        """Check if the user is in the booked_by field."""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return object.booked_by.filter(id=request.user.id).exists()
        return False
    def get_isAdmin(self, obj):
        """Check if the user is an admin."""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return request.user.is_staff
        return False
