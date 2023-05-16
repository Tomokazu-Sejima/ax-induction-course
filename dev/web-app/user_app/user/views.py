from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer


@api_view(["GET", "POST"])
def user_list(request):
    """
    List all code snippets, or create a new User.
    """
    if request.method == "GET":
        queryset = User.objects.all()
        employee_id = request.query_params.get("user_id", None)
        user_name = request.query_params.get("user_name", None)
        department = request.query_params.get("department", None)

        if employee_id is not None:
            queryset = queryset.filter(user_id__icontains=employee_id)
        if user_name is not None:
            queryset = queryset.filter(user_name__icontains=user_name)
        if department is not None:
            queryset = queryset.filter(department__icontains=department)

        serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def user_detail(request, pk):
    """
    Retrieve, update or delete a code User.
    """
    try:
        snippet = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        User.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
