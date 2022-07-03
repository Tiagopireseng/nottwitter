from rest_framework import serializers
from .models import Seguir, User, Tweet, Comentar


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')


class SeguirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguir
        fields = ('id', 'user', 'seguindo')

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('user','id','text')
        read_only=(  'created_at', 'updated_at','retweet_count', 'like_count','sharedtweet')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentar
        fields = ('id', 'tweet', 'user', 'text', 'created_at', 'updated_at')
