import re

from rest_framework import serializers

from .models import Employee

COMPANY_DOMAIN = "company.com"
EMP_ID_PATTERN = re.compile(r"^EMP\d+$")


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_email(self, value):
        domain = value.rsplit("@", 1)[-1].lower()
        if domain != COMPANY_DOMAIN:
            raise serializers.ValidationError(
                f"Email must be from the company domain (@{COMPANY_DOMAIN})."
            )
        return value

    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError("Salary must be positive.")
        return value

    def validate_emp_id(self, value):
        if not EMP_ID_PATTERN.match(value):
            raise serializers.ValidationError(
                "emp_id must be 'EMP' followed by numbers (e.g. EMP123)."
            )
        return value
