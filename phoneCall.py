from flask import Flask
app = Flask(__name__)

@app.route("/call/<tonum>")
def call__(tonum):
	from twilio.rest import Client
	account_sid = input("Enter your Twilio accountsid: ")
	auth_token = input("Enter your Twilio authtoken: ")
	client = Client(account_sid,auth_token)
	twilio_num = input("Enter your Twilio number: ")
	twiml_url = input("Enter your Twilio URL: ")
	call = client.calls.create(to=tonum, from_=twilio_num, url=twiml_url)
	return "call made."

app.run(prot='80',host ='0.0.0.0')
