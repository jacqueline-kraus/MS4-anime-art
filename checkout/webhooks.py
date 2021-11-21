from django.conf import settings
from django.http import HttpResponse, response
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import Stripe_Webhook_Handler

import stripe

@require_POST
@csrf_exempt
def webhook(request):
    
    """ Listen for webhooks """
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    """ code from stripe documentation https://stripe.com/docs/webhooks/signatures """
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)
    
    # set up a webhook handler
    handler = Stripe_Webhook_Handler(request)

    # map webhook events ro relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed,
    }

    # get the webhook type from stripe
    event_type = event['type']

    # if there is a handler for it then get it from the event map
    event_handler = event_map.get(event_type, handler.handle_event)

    # call the event handler with the event
    response = event_handler(event)
    return response