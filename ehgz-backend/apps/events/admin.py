from django.contrib import admin

from .models import Event, Category, Tag

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category']
    ordering = ['id']
    list_display = ['id','name']
    fieldsets = (
        (None, {'fields': ('name', 'description',)}),
        ('Category and Tags', {'fields': ('category', 'tags')}),
        ('Image', {'fields': ('image',)}),
        ('Price', {'fields': ('price',)}),
        ('Date', {'fields': ('date',)}),
        ('Venue', {'fields': ('venue',)}),
        ('Booked By', {'fields': ('booked_by',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'description', 'date', 'venue', 'category', 'tags', 'image', 'price', 'booked_by'),
        }),
    )
    search_fields = ('name', 'description')
    list_filter = ('category', 'tags')
    list_per_page = 10
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name']
    list_per_page = 10
    ordering = ['id']