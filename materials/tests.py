from rest_framework.test import APITestCase
from rest_framework import status
from materials.models import Course, Lesson
from users.models import User
from rest_framework.test import force_authenticate
from django.test.client import encode_multipart, RequestFactory
from django.urls import reverse


class CourseAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=1,
            name="testuser",
            email="testuser@test,com",
            phone_number="12345",
            city="testcity",
            password='12345'
        )
        self.course = Course.objects.create(
            id=10,
            name="CourseTest 1",
            description="CourseDescroption 1",
            user=self.user
        )
        self.lesson = Lesson.objects.create(
            id=1,
            name="LessonTest 1",
            description="Lesson Discription Test",
            link="youtube.com",
            course=self.course,
            user=self.user
        )

    def test_get_list_course(self):
        self.client.force_authenticate(user=self.user)
        responce = self.client.get(
            '/course/')
        self.assertEquals(
            responce.status_code,
            status.HTTP_200_OK
        )

    def test_create_course(self):
        data = {
            "name": "CourseTest 2",
            "description": "CourseDescroption 2",
            "user": self.user
        }
        self.client.force_authenticate(user=self.user)
        responce = self.client.post(
            '/course/',
            data=data)

        self.assertEquals(
            responce.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_course(self):
        self.client.force_authenticate(user=self.user)
        responce = self.client.delete(
            '/course/10/')

        self.assertEquals(
            responce.status_code,
            status.HTTP_204_NO_CONTENT
        )


    def test_get_list_lesson(self):
        self.client.force_authenticate(user=self.user)
        responce = self.client.get(
            '/lesson/')
        self.assertEquals(
            responce.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        data = {
            "name": "LessonTest 2",
            "description": "Lesson Discription Test 2",
            "user": self.user,
            "link": "youtube.com",
        }
        print(data)
        self.client.force_authenticate(user=self.user)
        responce = self.client.post(
            '/course/',
            data=data)
        print(responce)
        self.assertEquals(
            responce.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_lesson(self):
        self.client.force_authenticate(user=self.user)
        responce = self.client.delete(
            '/lesson/delete/1/')
        print(Lesson.objects.all())

        self.assertEquals(
            responce.status_code,
            status.HTTP_204_NO_CONTENT
        )
