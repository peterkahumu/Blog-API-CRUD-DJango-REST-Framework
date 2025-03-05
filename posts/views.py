from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

# class PostList(generics.ListCreateAPIView):
    
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly,]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class Userlist(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class PostViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer