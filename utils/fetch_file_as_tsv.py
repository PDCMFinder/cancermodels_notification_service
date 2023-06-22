import urllib.request


class fetch_files():
    def __init__(self):
        self.url = ''
        self.filename = 'temp.tsv'

    def fetch(self):
        urllib.request.urlretrieve(self.url, 'temp/' + str(self.filename))
