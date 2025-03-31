


class MessageService:
    
    # depencency object injected
    def __init__(self, sender):
        self.sender = sender

    def send_message(self,message):
        self.sender.send(message+"\n")


class EmailSender:

    def send(self, message):
        print(f"Senging email: {message}")

class SMSender:

    def send(self, message):
        print(f"Sending SMS: {message}")

    

if __name__ == "__main__":

    email_service = MessageService(EmailSender())
    email_service.send_message("Hello Saroj!!")

    sms_service = MessageService(SMSender())
    sms_service.send_message("Hello Saroj !!")


    