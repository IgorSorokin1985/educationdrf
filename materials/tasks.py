from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from celery import shared_task
from subscription.models import Subscription


@shared_task
def send_email_update_course(course):
    subscriptions = Subscription.objects.all().filter(course=course)
    users = []
    for subscription in subscriptions:
        users.append(subscription.user)
    for user in users:
        message = f"Hello {user.name}. {course.name} was updated."
        send_mail(
            subject="Course's update",
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
