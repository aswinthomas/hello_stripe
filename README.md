# hello_stripe

This repo introduces one of the basic use cases of using the Stripe API. This includes:

- Creating card token based on raw card details
- Creating and confirming a payment intent
- Capturing the payment intent

## Prerequisites

- `pip install stripe`
- `config.json` - Depending on the script chosen, you might need to create this file with the following contents:
  ```json
  {
    "stripe_secret_key": "sk_test_XXXX",
    "card_token_id": "tok_XXXX",
    "customer_id": "cus_XXXX",
    "payment_method_id": "card_XXXX",
    "payment_intent_id": "pi_XXXX"
  }
  ```
- `config.js` - Depending on the script chosen, you might need to create this file with the following contents:
  ```js
  var stripePublicKey = 'pk_XXXX';
  ```