

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomTokenObtainPairView, UserListCreateView, UserDetailView, SchoolListCreateView, SchoolDetailView, ClassListCreateView, ClassDetailView

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', UserListCreateView.as_view(), name='user_list_create'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('api/schools/', SchoolListCreateView.as_view(), name='school_list_create'),
    path('api/schools/<int:pk>/', SchoolDetailView.as_view(), name='school_detail'),
    path('api/classes/', ClassListCreateView.as_view(), name='class_list_create'),
    path('api/classes/<int:pk>/', ClassDetailView.as_view(), name='class_detail'),
]


