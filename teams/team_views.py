from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Team
from .serializers import TeamSerializer
from django.http import Http404


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# class TeamList(APIView):
#     """
#     List all teams or create a new team.
#     """
#
#     def get(self, request):
#         teams = Team.objects.all()
#         serializer = TeamSerializer(teams, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = TeamSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class TeamDetail(APIView):
#     """
#     Get, update, or delete a specific command.
#     """
#
#     def get_object(self, pk):
#         try:
#             return Team.objects.get(pk=pk)
#         except Team.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         team = self.get_object(pk)
#         serializer = TeamSerializer(team)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         team = self.get_object(pk)
#         serializer = TeamSerializer(team, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         team = self.get_object(pk)
#         team.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
