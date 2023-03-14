from django.urls import path
from .views import UserAPIView, SchoolAPIView, ClassAPIView

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='users'),
    path('schools/', SchoolAPIView.as_view(), name='schools'),
    path('classes/', ClassAPIView.as_view(), name='classes'),
]


