"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bookclubapi.models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""

    class Meta:
        model = Book
        fields = ("id", "title", "author", "image", "synopsis")


class BookView(ViewSet):
    """Book Club Membersview"""

    def list(self, request):
        """Handle GET requests to get all books

        Returns:
            Response -- JSON serialized list of members
        """

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
