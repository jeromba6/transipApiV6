from OpenSSL import crypto
import base64
import requests
import random
import string
import json

def randomDigits(self, stringLength=10):
    """Generate a random string of letters and digits """
    return ''.join(random.choice(string.digits) for i in range(stringLength))

class Generic:
    base_url='https://api.transip.nl/v6/auth'
    def __init__(self, login, key, demo = False):
        self.login = login
        self.key = key
        self.demo = demo

    def get_jwt(self):
        if self.demo:
            return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImN3MiFSbDU2eDNoUnkjelM4YmdOIn0.eyJpc3MiOiJhcGkudHJhbnNpcC5ubCIsImF1ZCI6ImFwaS50cmFuc2lwLm5sIiwianRpIjoiY3cyIVJsNTZ4M2hSeSN6UzhiZ04iLCJpYXQiOjE1ODIyMDE1NTAsIm5iZiI6MTU4MjIwMTU1MCwiZXhwIjoyMTE4NzQ1NTUwLCJjaWQiOiI2MDQ0OSIsInJvIjpmYWxzZSwiZ2siOmZhbHNlLCJrdiI6dHJ1ZX0.fYBWV4O5WPXxGuWG-vcrFWqmRHBm9yp0PHiYh_oAWxWxCaZX2Rf6WJfc13AxEeZ67-lY0TA2kSaOCp0PggBb_MGj73t4cH8gdwDJzANVxkiPL1Saqiw2NgZ3IHASJnisUWNnZp8HnrhLLe5ficvb1D9WOUOItmFC2ZgfGObNhlL2y-AMNLT4X7oNgrNTGm-mespo0jD_qH9dK5_evSzS3K8o03gu6p19jxfsnIh8TIVRvNdluYC2wo4qDl5EW5BEZ8OSuJ121ncOT1oRpzXB0cVZ9e5_UVAEr9X3f26_Eomg52-PjrgcRJ_jPIUYbrlo06KjjX2h0fzMr21ZE023Gw'
        pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, self.key)
        data = '{ "login": "' + self.login + '", "nonce": ' + randomDigits(10) + ' }'
        signature = base64.b64encode(crypto.sign(pkey, data.encode(), "sha512")).decode()
        headers = {'Signature': signature, 'Accept': 'application/json'}
        res = requests.post(self.base_url, headers=headers, data=data.encode())
        if res.status_code != 201:
            print('Could not create a JWT. Status_code was: ' + str(res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)['token']

    def get_headers(self):
       return {'Authorization': 'Bearer ' + Generic.get_jwt(self), 'Accept': 'application/json'}
