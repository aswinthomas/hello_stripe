import stripe
import json

# Load Stripe secret key from a JSON config file
with open('config.json') as json_file:
    data = json.load(json_file)
    stripe.api_key = data['stripe_secret_key']
    customer_id = data['customer_id']
    payment_method = data['payment_method']

# Create a PaymentIntent with capture_method set to manual
payment_intent = stripe.PaymentIntent.create(
  amount=10000, # amount in cents
  currency='usd',
  customer=customer_id, # replace with your customer id
  payment_method=payment_method,
  capture_method='manual',
)

print(payment_intent)
