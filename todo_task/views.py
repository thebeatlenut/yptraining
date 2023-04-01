from django.shortcuts import render


# Create your views here.
from todo_task.models import Task, Comment
from django.shortcuts import get_object_or_404
from todo_task.serializers import TaskSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response




class FirstFiveMixin:
    @action(detail=False, methods=['get'])
    def top_five(self, request):
        queryset = self.get_queryset()[:5]
        serializer_class = self.serializer_class
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)




class TaskViewSet(viewsets.ModelViewSet, FirstFiveMixin):
    """
    A viewset for viewing and editing Task instances.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()




class CommentViewSet(viewsets.ModelViewSet, FirstFiveMixin):
    """
    A viewset for viewing and editing Comment instances.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.prefetch_related('task').all()