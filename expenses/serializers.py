from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Income, Expense



class CategorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Category
        fields = ['id', 'user', 'name']



class IncomeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    category_name = serializers.ReadOnlyField(source='category.name', read_only=True)

    class Meta:
        model = Income
        fields = ['id', 'title', 'amount', 'date', 'remark', 'category', 'user']



class ExpenseSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    category_name = serializers.ReadOnlyField(source='category.name', read_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'date', 'remark', 'category', 'user']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for new user reg
    password as write-only to protect from displaying in responses
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user