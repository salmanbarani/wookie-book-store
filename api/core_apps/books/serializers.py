from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["pkid", "title", "description", "author", "cover_image", "price"]
        read_only_fields = ("pkid", "author")

    def get_author(self, obj):
        return obj.author.full_name
