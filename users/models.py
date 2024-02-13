from django.db import models
from django.contrib.auth.models import AbstractUser
from materials.models import Course, Lesson

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=50, verbose_name='Phone_number')
    city = models.CharField(max_length=50, verbose_name='City')
    avatar = models.ImageField(upload_to='users', **NULLABLE, verbose_name='Avater')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


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
