from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Book
from .pagination import BookPagination
from .permissions import IsMemberOfBannedGroup
from .serializers import BookSerializer


class BookOwnershipMixin(viewsets.ModelViewSet):
    def check_ownership(self, book, request):
        if book.author == request.user:
            return True
        raise PermissionDenied("book doesn't belong to you")


class BookViewSet(BookOwnershipMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsMemberOfBannedGroup]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "title": ["exact", "icontains"],
        "author__first_name": ["exact", "icontains"],
        "author__last_name": ["exact", "icontains"],
        "price": ["lte", "gte"],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        self.check_ownership(self.get_object(), request)
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.check_ownership(self.get_object(), request)
        return super().update(request, *args, **kwargs)
