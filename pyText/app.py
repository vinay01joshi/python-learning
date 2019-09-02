from twilio.rest import Client

account_sid = "__"
auth_token = "__"
client = Client(account_sid, auth_token)

call = client.messages.create(
    to="+918527686587",
    from_="+17074753543",
    body="this is first text"
)
print(call)
