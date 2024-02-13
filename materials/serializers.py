from rest_framework import serializers
from materials.models import Course, Lesson


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "link"]


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonsSerializer(source="lesson_set", many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "name", "description", "count_lessons", "lessons"]

    def get_count_lessons(self, instance):
        return len(Lesson.objects.all().filter(course=instance.pk))

    #def get_lessons(self, instance):
    #    return Lesson.objects.all().filter(course=instance.pk)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
