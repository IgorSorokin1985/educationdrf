from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from materials.models import Course
from subscription.models import Subscription
from django.shortcuts import get_object_or_404

# Create your views here.


class SubscriptionAPIView(APIView):

    def post(self, *args, **kwargs):
        user_id = self.request.user.pk
        course_id = self.request.data["course"]
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user_id).filter(course=course_id).all()

        if len(subs_item) > 0:
            subscription_id = subs_item[0].pk
            subscription = Subscription.objects.get(pk=subscription_id)
            subscription.delete()
            message = 'Subscription deleted'
        else:
            new_subscription = {
                "user_id": user_id,
                "course_id": course_id
            }
            Subscription.objects.create(**new_subscription)
            message = f'Subscription created {new_subscription}'
        return Response({"message": message})
