# -*- coding: utf-8 -*-
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from v1.third_party.rest_framework.permissions import IsStaffOrReadOnly
from ..models.user_earnings import UserEarnings
from ..serializers.user_earnings import UserEarningsSerializer


class UserEarningsViewSet(GenericViewSet, ListModelMixin):
    filterset_fields = ['repository', 'time_period']
    ordering = ['-total_amount']
    ordering_fields = ['total_amount']

    pagination_class = None
    permission_classes = [IsStaffOrReadOnly]

    queryset = UserEarnings.objects.select_related('user')
    serializer_class = UserEarningsSerializer
