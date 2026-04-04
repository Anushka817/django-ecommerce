import razorpay
from django.conf import settings
from django.shortcuts import render
from cart.models import CartItem

def checkout(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(i.total() for i in items)

    return render(request, 'orders/checkout.html', {
        'items': items,
        'total': total
    })


def place_order(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(i.total() for i in items)

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    payment = client.order.create({
        "amount": int(total * 100),
        "currency": "INR",
        "payment_capture": "1"
    })

    return render(request, 'orders/payment.html', {
'payment': payment,
'total': total
})



def order_history(request):
    return render(request, 'orders/history.html')