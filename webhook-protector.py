import hmac
import hashlib
from flask import Flask, request, abort

app = Flask(__name__)

# Replace this with your own secret key
secret_key = 'your_secret_key'

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Check if the request came from an allowed IP address or hostname
    allowed_origins = ['example.com', '123.456.789.0']
    origin = request.headers.get('Origin')
    if origin not in allowed_origins:
        abort(403)

    # Verify the payload using the secret key
    signature = request.headers.get('X-Hub-Signature')
    if not signature:
        abort(401)

    sha1 = hashlib.sha1()
    sha1.update(secret_key.encode())
    sha1.update(request.data)
    expected_signature = "sha1=" + sha1.hexdigest()

    if not hmac.compare_digest(expected_signature, signature):
        abort(401)

    # Handle the webhook payload here
    # ...

    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
