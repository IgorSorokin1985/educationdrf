from materials.views import CourseViewSet
from rest_framework.routers import DefaultRouter
from materials.apps import MaterialsConfig
from django.urls import path
from materials.views import LessonCreateAPIView, LessonDestroyAPIView, LessonListAPIView, LessonUpdateAPIView, LessonRetrieveAPIView, CoursePaymentAPIView
# Описание маршрутизации для ViewSet

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('course/payment/', CoursePaymentAPIView.as_view(), name='course_payment'),
] + router.urls
