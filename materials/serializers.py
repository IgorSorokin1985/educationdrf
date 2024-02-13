from rest_framework import serializers
from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lessons(self, instance):
        return len(Lesson.objects.all().filter(course=instance.pk))


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
