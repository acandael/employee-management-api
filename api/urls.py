from django.urls import path, include
# from .views import EmployeeView, EmployeeDetailView, EmployeeViewSet
from .views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
    # path("employees/", EmployeeView.as_view(), name="employees"),
    # path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee"),
]
