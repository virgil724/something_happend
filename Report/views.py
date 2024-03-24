from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from Group.models import Group, GroupLeader

from .serializers import ReportSerializer, CommentSerializer
from .models import Report, Comment
from rest_framework.response import Response

from rest_framework.filters import BaseFilterBackend


class ReportViewSets(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return Report.objects.filter(author=user)
        return Report.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_anonymous:
            serializer.save(author=None)
        else:
            serializer.save(author=self.request.user)


class CommentViewSetCUD(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_anonymous:
            serializer.save(author=None)
        else:
            serializer.save(author=self.request.user)


class ListCommentWithReport(viewsets.ViewSet):
    def list(self, request, pk=None, *args, **kwargs):
        return Response()

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Comment.objects.filter(report=pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)


class ReportByGroupView(generics.ListAPIView):
    serializer_class = ReportSerializer

    def get_queryset(self):
        group_pk = self.kwargs.get("pk")
        if group_pk:
            group = Group.objects.filter(pk=group_pk).first()

            if group:
                return Report.objects.filter(author__group=group)
        return Report.objects.none()


class ReportByManageGroup(generics.ListAPIView):
    serializer_class = ReportSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            group_leaders = GroupLeader.objects.filter(user=user)
            group_ids = [group_leader.group.id for group_leader in group_leaders]
            managed_groups = Group.objects.filter(id__in=group_ids)
            managed_members = [
                member for group in managed_groups for member in group.members.all()
            ]
            managed_reports = Report.objects.filter(author__in=managed_members)
            return managed_reports

            # print(groups)
        return Report.objects.none()


class ReportByUserId(generics.ListAPIView):
    serializer_class = ReportSerializer

    def get_queryset(self):
        user_pk = self.kwargs.get("pk")
        return Report.objects.filter(author=user_pk)
