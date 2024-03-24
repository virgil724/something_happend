from rest_framework import serializers
from .models import Group, Department, GroupLeader, DepartmentManager
from django.contrib.auth import get_user_model


class GroupSerializers(serializers.ModelSerializer):
    member_details = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = "__all__"

    def get_member_details(self, obj):
        member_details = []
        group_leader = None
        try:
            group_leader = GroupLeader.objects.get(group=obj).user
        except GroupLeader.DoesNotExist:
            pass

        for member in obj.members.all():
            is_leader = False
            if group_leader and member == group_leader:
                is_leader = True
            member_details.append(
                {"username": member.username, "id": member.id, "is_leader": is_leader}
            )
        return member_details


class GroupLeaderSerializers(serializers.ModelSerializer):
    username = serializers.StringRelatedField(read_only=True, source="user")
    groupname = serializers.StringRelatedField(read_only=True, source="group.name")

    class Meta:
        model = GroupLeader
        fields = "__all__"


class DepartmentSerializers(serializers.ModelSerializer):
    member_details = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = "__all__"

    def get_member_details(self, obj):
        member_details = []
        for member in obj.groups.all():
            member_details.append({"name": member.name, "id": member.id})
        return member_details


class DepartmentManagerSerializers(serializers.ModelSerializer):
    username = serializers.StringRelatedField(read_only=True, source="user")
    groupname = serializers.StringRelatedField(read_only=True, source="group.name")

    class Meta:
        model = DepartmentManager
        fields = "__all__"


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "id"]
