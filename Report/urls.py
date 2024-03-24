from django.urls import re_path, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

router = SimpleRouter()
router.register(r"report", views.ReportViewSets)
router.register(r"comment", views.CommentViewSetCUD)
router.register(
    r"comment/report", views.ListCommentWithReport, basename="comment_report"
)

urlpatterns = [
    path(
        "report/group/<int:pk>/",
        views.ReportByGroupView.as_view(),
        name="report-by-group",
    ),
    path("report/manage/", views.ReportByManageGroup.as_view()),
    path("report/user/<int:pk>", views.ReportByUserId.as_view()),
]

urlpatterns += router.urls
