import os
import requests
from requests.auth import HTTPProxyAuth
from pypac import PACSession, get_pac


pac = get_pac(url='')
session = PACSession(pac)
session = PACSession(proxy_auth=HTTPProxyAuth('user', 'pass'))



dirOrigem = '\Users\temp'

for arquivo in os.scandir(dirOrigem):
    f = open(dirOrigem  + arquivo.name, 'rb')
    files = {"file": f }
    resp = session.post("http://localhost:3999/file-upload", files = files)
    print(resp)
