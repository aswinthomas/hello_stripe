import stripe
import json

# Load Stripe secret key from a JSON config file
with open('config.json') as json_file:
    data = json.load(json_file)
    stripe.api_key = data['stripe_secret_key']
    card_token_id = data['card_token_id']

# Create a new customer and assign the card token
customer = stripe.Customer.create(
  description="Example customer",
  source=card_token_id
)

print(customer)
