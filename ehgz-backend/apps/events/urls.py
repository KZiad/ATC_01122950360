from django.urls import include, path
from .views import EventListView, EventDetailView, CategoryListView
urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('<int:pk>', EventDetailView.as_view(), name='event-detail'),
    path('category/', CategoryListView.as_view(), name='category-list'),
]
