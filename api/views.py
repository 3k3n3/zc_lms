from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import status
from accounts.models import CustomUser, Student, Mentor
from .serializers import StudentSerializer, CustomUserSerializer


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def overview(request):
    """Overview of API endpoints(in development)."""
    endpoints = {
        "Overview": "http://127.0.0.1:8000/api",
        "All Students": "http://127.0.0.1:8000/api/all/students",
        "All Students BE": "http://127.0.0.1:8000/api/all/students/be/",
        "All Students DZ": "http://127.0.0.1:8000/api/all/students/dz/",
        "All Students FE": "http://127.0.0.1:8000/api/all/students/fe/",
        "All Students MB": "http://127.0.0.1:8000/api/all/students/mb/",
        "Get Student": "http://127.0.0.1:8000/api/get/student/<pk>",
        "Add Student/Signup": "http://127.0.0.1:8000/api/signup",
        "pk": "User ID",
    }
    return Response(endpoints)


@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def all_students(request):
    """Get all students."""
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def all_students_dz(request):
    """Get all Design students."""
    students = Student.objects.filter(username__track="Design")
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def all_students_mb(request):
    """Get all Mobile students."""
    students = Student.objects.filter(username__track="Mobile")
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def all_students_fe(request):
    """Get all FrontEnd students."""
    students = Student.objects.filter(username__track="FrontEnd")
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def all_students_be(request):
    """Get all BackEnd students."""
    students = Student.objects.filter(username__track="BackEnd")
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def get_student(request, pk):
    """Get indivual student with id=pk."""
    try:
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def student_signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    else:
        print("error")
    return Response(serializer.data)
