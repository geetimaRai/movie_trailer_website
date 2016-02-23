from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACc2954918c1069732cab6d65b1fd47f28"
auth_token  = "3517101730f114a43af8cd4a6f21686b"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is Khan!",
                                 to="+1 5102061088",    # Replace with your phone number
                                 from_="+1 6505909119") # Replace with your Twilio number
print message.sid