from django.db import models
from django.conf import settings


# Create your models here.
class Report(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="report",
    )
    created = models.DateTimeField(auto_now_add=True)
    body = models.JSONField()


class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    body = models.JSONField()
