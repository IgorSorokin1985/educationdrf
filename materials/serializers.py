from rest_framework import serializers
from materials.models import Course, Lesson
from materials.validators import wrong_links_validator


class LessonsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[wrong_links_validator])
    description = serializers.CharField(validators=[wrong_links_validator])
    link = serializers.CharField(validators=[wrong_links_validator])

    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "link"]


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonsSerializer(source="lesson_set", many=True, read_only=True)
    name = serializers.CharField(validators=[wrong_links_validator])
    description = serializers.CharField(validators=[wrong_links_validator])
    link = serializers.CharField(validators=[wrong_links_validator])

    class Meta:
        model = Course
        fields = ["id", "name", "description", "count_lessons", "lessons"]

    def get_count_lessons(self, instance):
        return len(Lesson.objects.all().filter(course=instance.pk))


class LessonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[wrong_links_validator])
    description = serializers.CharField(validators=[wrong_links_validator])
    link = serializers.CharField(validators=[wrong_links_validator])

    class Meta:
        model = Lesson
        fields = '__all__'
