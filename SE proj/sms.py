from twilio.rest import Client


def sms(self, msg):
    account_sid = 'AC6c0e399c18b5bd01b138d38a3e489a4c'
    auth_token = '88c7e2639deba2cc75fe61d0851677a0'
    client = Client(account_sid, auth_token)
    FROM_NUM = '+917339445370'
    VERIFIED_NUMBER = '+91'
    message = client.messages.create(body='Hi there! How are you?', from_=FROM_NUM, to = VERIFIED_NUMBER)
    print(message.sid)




