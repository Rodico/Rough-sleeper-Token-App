# Configuration for PayPal
import paypalrestsdk

# PayPal API credentials
PAYPAL_MODE = "sandbox"  # Change to "live" in production
PAYPAL_CLIENT_ID = "YOUR_CLIENT_ID"
PAYPAL_CLIENT_SECRET = "YOUR_CLIENT_SECRET"

# Configure PayPal SDK
paypalrestsdk.configure({
    "mode": PAYPAL_MODE,
    "client_id": PAYPAL_CLIENT_ID,
    "client_secret": PAYPAL_CLIENT_SECRET
})
