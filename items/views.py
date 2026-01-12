import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Item
from .serializers import ItemSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(['GET'])
def buy_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': item.currency.lower(),
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f"{settings.DOMAIN}/items/success/",
            cancel_url=f"{settings.DOMAIN}/items/cancel/",
        )
        return Response({'id': session.id})
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    serializer = ItemSerializer(item)
    return render(request,
                  'items/item_detail.html',
                  {'item': serializer.data,
                   'stripe_public_key': settings.STRIPE_PUBLIC_KEY})


def home(request):
    items = Item.objects.all()
    return render(request, 'items/home.html', {'items': items})


def success(request):
    return render(request, 'items/success.html')


def cancel(request, item_id=None):
    return render(request, 'items/cancel.html', {'item_id': item_id})
