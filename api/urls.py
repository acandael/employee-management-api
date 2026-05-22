from django.urls import path
from .views import EmployeeView, EmployeeDetailView

urlpatterns = [
    path("employees/", EmployeeView.as_view(), name="employees"),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee"),
]
