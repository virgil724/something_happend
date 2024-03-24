from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import (
    GroupViewSets,
    DepartmentViewSets,
    GroupLeaderCreate,
    DepartmentManagerViewSets,
    UsersList,
    ManageGroup,
    ManageDepartment,
    GroupLeaderDelete,
)

router = SimpleRouter()
router.register(r"group", GroupViewSets)
router.register(r"department", DepartmentViewSets)
router.register(r"group_leader", GroupLeaderCreate)
router.register(r"depart_manager", DepartmentManagerViewSets)
router.register(r"users", UsersList)
urlpatterns = [
    path("group_leader/group/<int:pk>", GroupLeaderDelete.as_view()),
    path("managegroup/", ManageGroup.as_view()),
    path("managedepartment/", ManageDepartment.as_view()),
]
urlpatterns += router.urls
