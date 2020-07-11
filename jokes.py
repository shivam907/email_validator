import requests
url = "https://sv443.net/jokeapi/v2/joke/any"
r = requests.request('GET', url)
d = r.json()
print(d)
print(d['joke'])
