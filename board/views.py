from django.shortcuts import render
from .models import Post
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def make_post(request):
    serializer = MakePostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_post(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = ViewPostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = MakePostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def make_comment(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = CommentRequestSerializer(data=request.data) # 들어오는 데이터를 시리얼라이저로 보냄
    if serializer.is_valid():
        new_comment = serializer.save(post=post)
        response = CommentResponseSerializer(new_comment) # 응답용 시리얼라이저에 데이터 보냄

        return Response(response.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def view_comment(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    # filter 함수 : 조건에 맞는 객체를 필터링해서 가져옴.
    # 1개의 데이터만 가져올 수 있고, 2개 이상이나 0개의 데이터가 탐색되면 에러를 발생시키는 get과 다르게
    # 0개나 여러개의 데이터가 가져와져도 에러 발생시키지 않음
    serializer = CommentResponseSerializer(comments, many=True) # 응답용 시리얼라이저에 데이터 보냄

    return Response(serializer.data, status=status.HTTP_200_OK)