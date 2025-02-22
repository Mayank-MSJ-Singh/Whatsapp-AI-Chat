from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import chatTest as ct

app = Flask(__name__)
@app.route("/", methods=['POST', 'GET'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    resp.message(ct.chat(incoming_msg))
    return str(resp)

if __name__ == "__main__":
    app.run(port=8080)