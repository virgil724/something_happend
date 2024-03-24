"""
URL configuration for something_happend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import ApiRootView
from Group.urls import router as GroupRouter
from Report.urls import router as ReportRouter

RootView = ApiRootView()
RootView.add_router(GroupRouter)
RootView.add_router(ReportRouter)
extrapattern = [
    path("", include("Group.urls")),
    path("", include("Report.urls")),
    path("", RootView.as_view()),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include((extrapattern, "api_v1"), namespace="api_v1")),
    path("v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("v1/token/validate/", TokenVerifyView.as_view(), name="token_validate"),
    path("v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
]
