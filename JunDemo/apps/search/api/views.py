from django.db.models import Q
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from apps.search.api.serializers import AccountSerializer
from apps.search.models import Account

class AccountsList(generics.ListAPIView):

#    permission_classes = (IsAuthenticated, )
    serializer_class = AccountSerializer

    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'description', )

    def get_queryset(self):
        search_text = self.request.GET.get('search')
        if search_text:
            fixed_q = Q(name__icontains=search_text) | \
                Q(delivery_director__username__icontains=search_text) | \
                Q(description__icontains=search_text)
            return Account.objects.filter(fixed_q ) 
        return Account.objects.all()

