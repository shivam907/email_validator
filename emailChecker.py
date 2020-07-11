# https://api.hunter.io/v2/email-verifier?email=shivam@cez.co.in&api_key=27ad6b2410afdd93b82abc5b6e48384f942c952d

import requests
url = "https://api.hunter.io/v2/email-verifier?email="+input("Enter Mail ID-   ")+"&api_key=27ad6b2410afdd93b82abc5b6e48384f942c952d"
r = requests.request('GET', url)
d = r.json()
print(d["data"]["result"])