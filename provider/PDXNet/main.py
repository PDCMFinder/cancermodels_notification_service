from utils import API
from provider.PDXNet import transform
from utils import send_email
class PDXNet():
    def __init__(self):
        self.API = API.API()
        self.transform = transform.PDXNet_data_transformations()

    def request(self):
        response = self.API.request()

    def main(self):
        self.transform.process_models()
        self.transform.compare_models()
        if self.transform.flag:
            send_email.send('Hi, \nNew models are available in PDXNet portal.\n\nTotal new Models: '
                            + str(len(self.transform.new_models)) + "\n\nModel IDs:"
                            + ", ".join(self.transform.new_models)
                            +"\nCheers", 'PDXNet Portal new models available.')
            self.transform.transform()
