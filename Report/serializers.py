from rest_framework import serializers
from .models import Report, Comment


class ReportSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Report
        fields = "__all__"
        read_only_fields = ("id", "author", "created")


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ("id","author","report", "body")
