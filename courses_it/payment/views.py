from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course
import uuid
import stripe
from .models import Purchase
import os


stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

class ParchaseView:
    @login_required
    def payment_process(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        
        if request.method == 'POST':
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': course.title,
                        },
                        'unit_amount': int(course.price * 100),  
                    },
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/payment/success/') 
                + '?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri('/payment/cancel/'),
                metadata={
                    'course_id': str(course.id),
                    "user_id": str(request.user.id),   
                }
            )
            return redirect(checkout_session.url, code=303)

        return render(request, 'payment.html', {'course': course})
            
    @login_required
    def payment_success(self, request):
        return render(request, "payment_success.html")

    @login_required
    def payment_cancel(self, request):
        return render(request, "payment_cancel.html")
    
    