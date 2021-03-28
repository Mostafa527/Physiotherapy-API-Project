from rest_framework import serializers
from .models import *
from rest_framework import serializers
from .models import Game
from django.contrib.auth.models import User
from Accounts.models import NewUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    Game_Owner = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail',read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = NewUser
        fields = ['id', 'username', 'posts', 'owner']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Game
        fields = ['url', 'owner', 'id', 'Name', 'Description',]

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Description = validated_data.get('Description', instance.Description)

        instance.save()
        return instance
class GameSerializer(serializers.ModelSerializer):


    class Meta:
        model = Game
        fields = ('id', 'Name', 'Description', 'owner',)