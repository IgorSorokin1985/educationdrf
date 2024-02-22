from rest_framework.routers import DefaultRouter
from subscription.apps import SubscriptionConfig
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from subscription.views import SubscriptionAPIView
# Описание маршрутизации для ViewSet

app_name = SubscriptionConfig.name

urlpatterns = [
    path('subscription/', SubscriptionAPIView.as_view(), name='subscription'),
]
