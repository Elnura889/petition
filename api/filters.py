import django_filters
from .models import Petition

class PetitionFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    created_at = django_filters.DateFilter(field_name='created_at', lookup_expr='exact')
    vote_count = django_filters.NumberFilter(field_name='vote_count', lookup_expr='exact')

    class Meta:
        model = Petition
        fields = ['title', 'created_at', 'vote_count']
