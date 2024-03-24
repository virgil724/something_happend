from django.db import models

# Create your models here.
from django.conf import settings


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="group", null=True, blank=True
    )


class GroupLeader(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="group_leader"
    )
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name="leader")


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    groups = models.ManyToManyField(
        Group, related_name="Department", null=True, blank=True
    )


class DepartmentManager(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="department_leader",
    )
    department = models.OneToOneField(
        Department, on_delete=models.CASCADE, related_name="leader"
    )
