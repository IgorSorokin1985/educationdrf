from django.db import models
from materials.models import Course, Lesson
from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):
    METHODS = (
        ("C", "Cash"),
        ("T", "Translation")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    date = models.DateField(verbose_name="Date of payment")
    course = models.ForeignKey(Course, **NULLABLE, on_delete=models.SET_NULL, verbose_name="Course")
    lesson = models.ForeignKey(Lesson, **NULLABLE, on_delete=models.SET_NULL, verbose_name="Lesson")
    amount = models.PositiveIntegerField(verbose_name="Amount")
    method = models.CharField(max_length=1, choices=METHODS)
