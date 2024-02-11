from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Course name')
    course_image = models.ImageField(upload_to='course', verbose_name='Course image')
    description = models.TextField(verbose_name='Course description')
    #link = models.CharField(max_length=200, verbose_name='Course link')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Lesson name')
    lesson_image = models.ImageField(upload_to='course', verbose_name='Lesson image')
    description = models.TextField(verbose_name='Lesson description')
    link = models.CharField(max_length=200, verbose_name='Lesson link')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course pk')

    def __str__(self):
        return f'Lesson - {self.name}'

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
