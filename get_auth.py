import base64
import requests
import json
import urllib3
def get_auth_token():
    """enter secret + BASE64Encode+ pass token """
    global url1
    https = "https://"
    url1 = input('Enter Bomgar FQDN:\n')
    url2 = ".beyondtrustcloud.com/oauth2/token"
    url = https + url1 + url2
    payload = 'grant_type=client_credentials'
    username= input('ClientID\n')
    password= input('ClientSecret\n')
    base64string = base64.encodebytes(('%s:%s' % (username, password)).encode('utf8')).decode('utf8').replace('\n', '')
    headers = {'authorization' : 'Basic %s' %base64string,
 'Content-Type':'application/x-www-form-urlencoded'}
    r = requests.request("POST", url, headers=headers, data = payload)
    json_data=r.json()
    global format
    for x in json_data :
        token = []
        format = json_data['access_token']
get_auth_token()
