from django.db import models


class Employee(models.Model):
    emp_id = models.CharField(max_length=10, unique=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    data_joined = models.DateField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.emp_id:
            return super().save(*args, **kwargs)
        # New record: save once to obtain the auto primary key, then
        # derive emp_id from it (e.g. EMP001) and update that one column.
        super().save(*args, **kwargs)
        self.emp_id = f"EMP{self.pk:03d}"
        super().save(update_fields=["emp_id"])
