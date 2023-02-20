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
			is_staff=validated_data.get('is_staff', False),
			is_superuser=validated_data.get('is_superuser', False),
		)
		user.set_password(validated_data['password'])
		user.save()

		return user

	class Meta:
		model = get_user_model()
		fields = ('id','email', 'first_name', 'last_name', 'password', 'is_staff', 'is_superuser')


class UserInfoSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'full_name', 'is_superuser')
        extra_kwargs = {'email': {'required': False}}

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
		is_active = validated_data.get('is_active')
		is_staff = validated_data.get('is_staff')
		is_superuser = validated_data.get('is_superuser')
		user = User.objects.create(
			email=validated_data['email'],
			first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=validated_data.get(is_staff, False),
			is_superuser=validated_data.get(is_superuser, False)
		)
		user.set_password(validated_data['password'])
		user.save()
		return user

	class Meta:
		model = get_user_model()
		fields = ('id', 'email', 'first_name', 'last_name', 'password','is_superuser', 'date_joined', 'is_active', 'is_staff')
