from rest_framework import serializers
from .models import Post, Comment
from django.utils import timezone

class MakePostSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at']

    def get_created_at(self, obj):
        return obj.created_at.date() # obj: 우리가 갖고 있는 데이터 객체

class CommentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']

    def get_created_at(self, obj):
        return obj.created_at.date()
    
class CommentResponseSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_created_at(self, obj):
        time = timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d')

class ViewPostSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    comments = CommentResponseSerializer(many=True, read_only=True)
    # 역참조하려면 아까 정의했던 related_name을 가지는 변수에, 원하는 return값 필드들을 가지는 시리얼라이저를 넣으면 됨
    # 여러 댓글을 시리얼라이저에 넣을 것이기 때문에 many=True
    # 단순히 댓글들을 조회해서 뱉는 역할만 하면 되므로 read_only=True

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at', 'comments']

    def get_created_at(self, obj):
        return obj.created_at.date() # obj: 우리가 갖고 있는 데이터 객체
    

class PostListSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    #comments = CommentResponseSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
    
    def get_created_at(self, obj):
        return obj.created_at.date() # obj: 우리가 갖고 있는 데이터 객체