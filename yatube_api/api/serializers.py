from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Group, Post, Comment, Follow


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'slug', 'description', 'id')
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('text', 'pub_date', 'author', 'group', 'id')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('author', 'text', 'created', 'post', 'id')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('following', 'user', 'id')
        model = Follow
