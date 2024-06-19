from rest_framework.serializers import ModelSerializer
from DRLapp.models import *
from DRLapp import paginators


class RegulationSerializer(ModelSerializer):
    class Meta:
        model = Regulation
        fields = ["id", "created_date", "active", "name"]


class FalcutySerializer(ModelSerializer):
    class Meta:
        model = Falcuty
        fields = ['id', 'name']


class ClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class UserSerializer(ModelSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['avatar'] = instance.avatar.url
        return rep

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(data["password"])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class ActivitySerializer(ModelSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = instance.image.url
        return rep

    class Meta:
        model = Activity
        fields = ['id', 'name', 'description', 'image', 'created_date', 'point', 'regulation']


class PointSerializer(ModelSerializer):
    class Meta:
        model = Point
        fields = ['id', 'confirm', 'point', 'user']

# class PointDetailSerializer(ModelSerializer):
#     user = UserSerializer(many=True)
#
#     class Meta:
#         model = PointSerializer.Meta.model
#         fields = []




