import stripe
import json

# Load Stripe secret key from a JSON config file
with open('config.json') as json_file:
    data = json.load(json_file)
    stripe.api_key = data['stripe_secret_key']
    payment_intent_id = data['payment_intent_id']

# Capture a portion of the authorized amount
payment_intent = stripe.PaymentIntent.capture(
  payment_intent_id,
  amount_to_capture=7500, # amount in cents
)

print(payment_intent)
