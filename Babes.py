from twilio.rest import Client

account_sid = 'AC39de526979864a3509de545b55490389'
auth_token = 'b114e87f8e1501ce88c8a5703c3084cd'
client = Client(account_sid, auth_token)
def send_love():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hey babes love',
        to='whatsapp:+27657276868'
    )

    print(message.sid)