from django.http import HttpResponse

class Stripe_Webhook_Handler:
    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )
    
    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charge[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        
        order_exists = False
        try:
            order = Order.objects.get(
                first_name_iexact=shipping_details.name,
                email_iexact=shipping_details.email,
                street_address_iexact=shipping_details.line1,
                postcode_iexact=shipping_details.postal_code,
                city_iexact=shipping_details.city,
                country_iexact=shipping_details.country,
                grand_total=grand_total,
            )
            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already exists in database',
                status=200)
        except Order.DoesNotExist:
            try:
                order = Order.objects.create(
                    first_name=shipping_details.name,
                    email=shipping_details.email,
                    street_address=shipping_details.line1,
                    postcode=shipping_details.postal_code,
                    city=shipping_details.city,
                    country=shipping_details.country,
                    grand_total=grand_total,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]} | ERROR {e}',
                                    status=500)
        
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
    
    def handle_payment_intent_failed (self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
        