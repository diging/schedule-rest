from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	def create(self, validated_data):
		for k,v in validated_data.items():
			print(k,v)
		user = User.objects.create(
			email=validated_data['email'],
			first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
		)
		user.set_password(validated_data['password'])
		user.save()

		return user

	class Meta:
		model = get_user_model()
		fields = ('id','email', 'first_name', 'last_name', 'password') 


class UserInfoSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = get_user_model()
        fields = ('id','email', 'first_name', 'last_name', 'full_name') 
    def get_full_name(self, obj):
        return obj.first_name + " " + obj.last_name

class UserInfoTransSerializer(serializers.Serializer):
    full_name = serializers.SerializerMethodField()
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    id = serializers.IntegerField()

    def get_full_name(self, obj):
        return obj.first_name + " " + obj.last_name


class UserSerializerAdminAccess(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	def create(self, validated_data):
		for k,v in validated_data.items():
			print(k,v)
		user = User.objects.create(
			email=validated_data['email'],
			first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=validated_data.get('is_active'),
            is_staff=validated_data.get('is_staff'),
		)
		user.set_password(validated_data['password'])
		user.save()
		return user

	class Meta:
		model = get_user_model()
		fields = ('id','email', 'first_name', 'last_name', 'password', 'date_joined', 'is_active', 'is_staff')
