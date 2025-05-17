import json
from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField, CharField
from rest_framework import serializers
from .models import Event, Category, Tag
import rest_framework.serializers as serializers

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


class EventCreateUpdateSerializer(ModelSerializer):
    # Accept category ID from frontend
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())

    # Accept a stringified JSON array from multipart (e.g. '["tag1", "tag2"]')
    tags = serializers.CharField(write_only=True, required=False)

    # Readable display for tags
    tags_display = serializers.SerializerMethodField(read_only=True)
    # Readable display for category
    category_display = serializers.SerializerMethodField(read_only=True)
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
            'category_display',
            'date',
            'venue',
            'price',
            'image',
            'tags',
            'tags_display',
            'booked'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', '[]')
        event = Event.objects.create(**validated_data)
        tag_objs = self._process_tags(tags_data)
        event.tags.set(tag_objs)
        return event

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if tags_data is not None:
            tag_objs = self._process_tags(tags_data)
            instance.tags.set(tag_objs)

        return instance
    def get_booked(self, obj):
        object = Event.objects.get(id=obj.id)
        """Check if the user is in the booked_by field."""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return object.booked_by.filter(id=request.user.id).exists()
        return False
    def get_tags_display(self, obj):
        return [tag.name for tag in obj.tags.all()]
    
    def get_category_display(self, obj):
        return obj.category.name if obj.category else None

    def _process_tags(self, tag_string):
        try:
            tag_names = json.loads(tag_string)
        except json.JSONDecodeError:
            raise serializers.ValidationError(
                {"tags": "Tags must be a JSON array of strings."})

        if not isinstance(tag_names, list) or not all(isinstance(t, str) for t in tag_names):
            raise serializers.ValidationError(
                {"tags": "Each tag must be a string."})

        tag_objs = []
        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name.strip())
            tag_objs.append(tag)
        return tag_objs


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
