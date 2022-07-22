import os
import sys
import requests

print(os.getcwd())
directory = os.path.join(os.getcwd(), 'facebook.ico')

url = 'https://wHoww.facebook.com/favicon.ico'
r = requests.get(url, allow_redirects=True)

open(directory, 'wb').write(r.content)

