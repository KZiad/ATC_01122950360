from .views import (
    CustomUserDetailsView,
    CustomLoginView,
    VerifyTokenView,
)
from django.urls import path
urlpatterns = [
    path('token/verify/', VerifyTokenView.as_view(), name='verify-token'),
    path('user/', CustomUserDetailsView.as_view(), name='user-details'),
    # path('token/refresh/', include('rest_framework_simplejwt.urls')),
]
