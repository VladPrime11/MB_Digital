from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Person
from .serializers import PersonSerializer
from django.http import Http404


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# class PersonList(APIView):
#     """
#     List all people or create a new person.
#     """
#
#     def get(self, request):
#         people = Person.objects.all()
#         serializer = PersonSerializer(people, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PersonDetail(APIView):
#     """
#     Get, update, or delete a specific person.
#     """
#
#     def get_object(self, pk):
#         try:
#             return Person.objects.get(pk=pk)
#         except Person.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         person = self.get_object(pk)
#         serializer = PersonSerializer(person)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         person = self.get_object(pk)
#         serializer = PersonSerializer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk):
#         person = self.get_object(pk)
#         serializer = PersonSerializer(person, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         person = self.get_object(pk)
#         person.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
