import stripe 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from courses.models import Course
from .models import Purchase
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, 
            sig_header, 
            os.getenv('STRIPE_WEBHOOK_SECRET')
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']


        if session['mode'] == 'payment'and session['payment_status'] == 'paid':
            course_id = session['metadata'].get('course_id')
            user_id = session['metadata'].get('user_id')
            try:
                course = Course.objects.get(id=course_id)
            except Course.DoesNotExist:
                return HttpResponse(status=400)
            

            Purchase.objects.update_or_create(
                payment_id=session['payment_intent'],
                defaults={
                    "user_id": user_id,
                    "course": course,
                    "amount": course.price,
                    "status": "success",
                },
            )
    return HttpResponse(status=200)