import datetime

from django.db import transaction
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets

from borrowing.models import Borrowing
from borrowing.serializers import (
    BorrowingSerializer,
    BorrowingListSerializer,
    BorrowingRetrieveSerializer,
    BorrowingCreateSerializer,
)
from rest_framework.response import Response


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        if self.action in ("retrieve", "return_book"):
            return BorrowingRetrieveSerializer
        if self.action == "create":
            return BorrowingCreateSerializer

        return self.serializer_class

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "user_id",
                type=OpenApiTypes.INT,
                description="Filter by user`s id, for admins only",
            ),
            OpenApiParameter(
                "is_active",
                type=OpenApiTypes.STR,
                description="Filter by borrowing actual return, "
                "?is_active=false to get not active borrowings, "
                "?is_active=true for active borrowings",
            ),
        ]
    )
    def get_queryset(self):
        queryset = self.queryset
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        user_id = self.request.query_params.get("user_id", None)
        is_active = self.request.query_params.get("is_active", None)
        if self.request.user.is_staff and user_id:
            queryset = queryset.filter(user__id=user_id)
        if is_active == "true":
            queryset = queryset.filter(actual_return__isnull=True)
        if is_active == "false":
            queryset = queryset.filter(actual_return__isnull=False)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, borrow_date=datetime.date.today())

    @action(
        methods=["get"],
        detail=True,
        permission_classes=[
            IsAdminUser,
        ],
        url_path="return",
        url_name="return_book",
    )
    def return_book(self, request, pk=None):
        """Endpoint for returning book, if book is already returned, return appropriate message"""
        with transaction.atomic():
            borrowing = self.get_object()
            if not borrowing.actual_return:
                borrowing.book.inventory += 1
                borrowing.book.save()
                actual_return = datetime.date.today()
                serializer = self.get_serializer_class()(
                    borrowing, data={"actual_return": actual_return}, partial=True
                )
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=200)
            return Response({"actual_return": "book has already returned"}, status=200)
