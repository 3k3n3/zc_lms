from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from accounts.models import CustomUser, Student, Mentor
from .serializers import StudentSerializer, CustomUserSerializer


@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def get_all_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def student_signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    else:
        print("error")
    return Response(serializer.data)
