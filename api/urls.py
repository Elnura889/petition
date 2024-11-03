from django.urls import path
from .views import PetitionListCreateView, VoteCreateView, VoteDeleteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('petitions/', PetitionListCreateView.as_view(), name='petition-list-create'),
    path('votes/', VoteCreateView.as_view(), name='vote-create'),
    path('votes/<int:pk>/', VoteDeleteView.as_view(), name='vote-delete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
