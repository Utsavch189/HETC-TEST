import requests

api_key="rL7Ps5AKZyHuMDgJfxYbVFeIBo1pUX4ac9NOCQvz2St8qWET3h2D9s7xEIPuKl6JqoyBOWmbizSnvT3L"

class SendSms:
    def __init__(self,number,message):
        self.header={
            "authorization":api_key,
            "Content-Type":"application/json"
        }
        self.number=number
        self.message=message
        self.url="https://www.fast2sms.com/dev/bulkV2"

    def send(self):
        body={
            "route" : "q",
            "sender_id" : "",
            "message" : self.message,
            "language" : "english",
            "flash" : 0,
            "numbers" : self.number,
        }
        requests.post(url=self.url,headers=self.header,json=body)

