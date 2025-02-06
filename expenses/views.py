from rest_framework import viewsets, permissions, status
from django.shortcuts import render
from .models import Category, Income, Expense
from .serializers import CategorySerializer, IncomeSerializer, ExpenseSerializer, UserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.authtoken.models import Token
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """
    List, create, retrieve, update and delete categories
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class IncomeViewSet(viewsets.ModelViewSet):
    """
    CRUD for income objects
    """
    serializer_class = IncomeSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Expense objects, accessible only to the owner.
    """
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter expenses by the current user
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class UserViewSet(viewsets.GenericViewSet):
    """
    minimal viwset for user registration
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classed = [permissions.AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_excepton=True)
        user = serializer.save()
        Token.objects.create(user=user)
        return Response(
            {
                "message": "User created successfully",
            }, status=status.HTTP_201_CREATED
        )
    

class LoginView(APIView):
    """
    customize login and gain token
    """
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        username = self.request.data['username']
        password = self.request.data['password']
        user = authenticate(username=username, password=password)
        
        if user:
            return Response({
                "token": user.auth_token.key,
            })
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)