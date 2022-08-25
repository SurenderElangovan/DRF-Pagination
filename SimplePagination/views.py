from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Post
from .serializers import PostSerializer

def index(request):
    return render(request, 'index.html')

class PostPagination(PageNumberPagination):
    page_size = 2

class PostViewSet(viewsets.ModelViewSet):
    pagination_class = PostPagination
    serializer_class = PostSerializer
    queryset = Post.objects.all()