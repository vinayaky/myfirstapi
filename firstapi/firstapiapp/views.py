from rest_framework import viewsets,status
from .models import UserProfile
from .serializers import UserSerializer,registerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class registeruser(APIView):
    def post(self, request):
        serializer = registerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=User.objects.get(username=serializer.data['username']) 
            token_obj, _ = Token.objects.get_or_create(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
   

class UserProfileView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def patch(self, request):
    
        try:
            profile = UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(profile, data=request.data, partial=True)
 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserSerializer
