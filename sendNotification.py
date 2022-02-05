from twilio.rest import Client

sid = 'AC9c86dc17a0164d1ecba9c0cfad2b97bc'
auth_token = '20eb0ea2090178931b89eb94ab839fb3'
# authenticate our phone
client = Client(sid, auth_token)


class Notification:

    def __init__(self):
        pass

    def verification_message(self):
        message = client.messages.create(to='whatsapp:+Your Phone Number',
                                              from_='whatsapp:+14155238886',
                                              body='We received your oder!')

    def ready_message(self):
        message = client.messages.create(to='whatsapp:+Your Phone Number',
                                              from_='whatsapp:+14155238886',
                                              body='Your edited photographs are ready!')


def main():
    message = Notification
    message.ready_message(message)


if __name__ == "__main__":
    main()
