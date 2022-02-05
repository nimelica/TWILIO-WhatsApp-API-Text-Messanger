from twilio.rest import Client

sid = 'copy and paste account sid from Twilio'
auth_token = 'add your authentication tokenize number here from Twilio'
# authenticate our phone
client = Client(sid, auth_token)


class Notification:

    def __init__(self):
        pass

    def verification_message(self):
        message = client.messages.create(to='whatsapp:+Your Phone Number',
                                              from_='whatsapp:+14155238886',
                                              body='We received your order!')

    def ready_message(self):
        message = client.messages.create(to='whatsapp:+Your Phone Number',
                                              from_='whatsapp:+14155238886',
                                              body='Your Order is Ready!')


def main():
    message = Notification
    message.ready_message(message)


if __name__ == "__main__":
    main()
