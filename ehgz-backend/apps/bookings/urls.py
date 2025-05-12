from django.urls import include, path
from .views import BookingCreateView
urlpatterns = [
    path('<int:pk>', BookingCreateView.as_view(), name='booking')
    
]
