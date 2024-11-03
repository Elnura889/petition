from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Petition, Vote
from .serializers import PetitionSerializer, VoteSerializer
from .filters import PetitionFilter

class PetitionListCreateView(generics.ListCreateAPIView):
    queryset = Petition.objects.all()
    serializer_class = PetitionSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PetitionFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        petition_id = self.request.data.get('petition')
        petition = Petition.objects.get(id=petition_id)

        # Check if the user has already voted for this petition
        if Vote.objects.filter(user=self.request.user, petition=petition).exists():
            return Response({'detail': 'You have already voted for this petition.'}, status=status.HTTP_400_BAD_REQUEST)

        # Increment vote count for the petition
        petition.vote_count += 1
        petition.save()

        serializer.save(user=self.request.user)

class VoteDeleteView(generics.DestroyAPIView):
    queryset = Vote.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_destroy(self, instance):
        petition = instance.petition
        petition.vote_count -= 1  # Decrement the vote count
        petition.save()
        instance.delete()
