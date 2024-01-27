from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from .models import User, Teacher
from .serializer import UserSerializer, TeacherSerializer


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_user_view(request):
    user = User.objects.all()
    ser_data = UserSerializer(user, many=True).data
    return Response(ser_data)


@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def gp_user_view(request):
    if request.method == 'GET':
        user = User.objects.all()
        ser_data = UserSerializer(user, many=True).data
        return Response(ser_data)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            phone_number=phone_number,
            email=email
        )
        return Response({'message': 'Created user'})


class TeacherList(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
