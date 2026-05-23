import django_filters

from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='From EMP ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='To EMP ID')
    salary_min = django_filters.NumberFilter(field_name='salary', lookup_expr='gte', label='From Salary')
    salary_max = django_filters.NumberFilter(field_name='salary', lookup_expr='lte', label='To Salary')


    class Meta:
        model = Employee
        fields = ['designation', 'name', 'id_min', 'id_max']

    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset
