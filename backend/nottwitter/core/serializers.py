from rest_framework import serializers
from .models import User, Tweet, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id','text')
        read_only=( 'user', 'created_at', 'updated_at','retweet_count', 'like_count','sharedtweet')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'tweet', 'user', 'text', 'created_at', 'updated_at')
