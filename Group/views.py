from django.shortcuts import render

# Create your views here.

from .models import Group, Department, GroupLeader, DepartmentManager
from .serializers import (
    GroupSerializers,
    DepartmentSerializers,
    GroupLeaderSerializers,
    DepartmentManagerSerializers,
    UserSerializers,
)
from rest_framework import viewsets, mixins, generics, status

from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.http import Http404


class GroupViewSets(viewsets.ModelViewSet):
    serializer_class = GroupSerializers
    queryset = Group.objects.all()


class DepartmentViewSets(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializers
    queryset = Department.objects.all()


class GroupLeaderCreate(viewsets.GenericViewSet, mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class = GroupLeaderSerializers
    queryset = GroupLeader.objects.all()


class GroupLeaderDelete(generics.DestroyAPIView):
    serializer_class = GroupLeaderSerializers
    queryset = GroupLeader.objects.all()

    def delete(self, request, *args, **kwargs):
        group_pk = kwargs.get("pk")
        group = Group.objects.filter(pk=group_pk).first()

        if group:
            try:
                group_leader = group.leader
                group_leader.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except GroupLeader.DoesNotExist:
                return Response(
                    {"error": "Group leader not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"error": "Group not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def get_object(self):
        group_pk = self.kwargs.get("pk")
        group = Group.objects.filter(pk=group_pk).first()
        if group:
            try:
                return group.leader
            except GroupLeader.DoesNotExist:
                raise Http404
        raise Http404


class DepartmentManagerViewSets(viewsets.ModelViewSet):
    serializer_class = DepartmentManagerSerializers
    queryset = DepartmentManager.objects.all()


class UsersList(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = UserSerializers
    queryset = get_user_model().objects.all()


class ManageGroup(generics.ListAPIView):
    serializer_class = GroupSerializers

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            group_leaders = GroupLeader.objects.filter(user=user)
            group_ids = [group_leader.group.id for group_leader in group_leaders]
            return Group.objects.filter(id__in=group_ids)
        return Group.objects.none()


class ManageDepartment(generics.ListAPIView):
    serializer_class = DepartmentSerializers

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return Department.objects.filter(leader=user)
        return Department.objects.none()
