import stripe
from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product

# Load Stripe Secret Key
stripe.api_key = settings.STRIPE_SECRET_KEY


PRODUCT = {
    "id": 1,
    "name": "Demo Product",
    "description": "A dummy product for testing payments.",
    "price": 5000,  # Price in cents
    "image_url": "https://via.placeholder.com/150"
}


def home(request):
    return render(request, 'home.html')

def succes(request):
    return render(request, 'succes.html')

@api_view(['GET'])
def get_product(request):
    return Response(PRODUCT)

#  API: Create Stripe Payment Intent
@api_view(['POST'])
def create_payment_intent(request):
    try:
        intent = stripe.PaymentIntent.create(
            amount=PRODUCT['price'],
            currency="usd",
            payment_method_types=["card"]
        )
        return Response({"client_secret": intent.client_secret})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#  API: Confirm Payment
@api_view(['POST'])
def confirm_payment(request):
    payment_intent_id = request.data.get("payment_intent_id")
    try:
        intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        if intent.status == "succeeded":
            return Response({
                "order_id": intent.id,
                "product": PRODUCT,
                "payment_status": "Success",
                "transaction_id": intent.id
            })
        else:
            return Response({"error": "Payment not successful"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Render Product Page
def product_page(request):
    return render(request, 'product.html', {"product": PRODUCT, "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY})
