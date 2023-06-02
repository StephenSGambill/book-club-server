"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bookclubapi.models import Member
from django.contrib.auth.models import User


class MemberUserSerializer(serializers.ModelSerializer):
    """ """

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class MemberSerializer(serializers.ModelSerializer):
    """JSON serializer for members"""

    user = MemberUserSerializer(many=False)

    class Meta:
        model = Member
        fields = ("id", "user", "bio", "profile_pic", "is_staff", "user")


class MemberView(ViewSet):
    """Book Club Membersview"""

    def list(self, request):
        """Handle GET requests to get all members

        Returns:
            Response -- JSON serialized list of members
        """

        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle Get requests to get single member

        Returns:
            Response -- JSON serialized instance of member
        """
        try:
            member = Member.objects.get(user=pk)
            print(member)
            serializer = MemberSerializer(member)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Member.DoesNotExist:
            return Response(
                {"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND
            )

        except Exception as ex:
            return Response(
                {"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def update(self, request, pk):
        """Handle PUT requests for member update

        Returns:
            Response -- Empty body with 204 status code
        """

        member = Member.objects.get(pk=pk)
        member.bio = request.data["bio"]
        member.profile_pic = request.data["profile_pic"]
        member.save()

        user = User.objects.get(pk=member.user_id)
        user.email = request.data["user"]["email"]
        user.first_name = request.data["user"]["first_name"]
        user.last_name = request.data["user"]["last_name"]
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
