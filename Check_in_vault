def check():
    global myid
    https = "https://"
    url2 = ".beyondtrustcloud.com/api/config/v1/vault/account"
    url = https + url1 + url2
    payload = {}
    headers = {
  'Authorization':  'Bearer %s' %format,

}
    r22 = requests.request("GET", url, headers=headers, data = payload)
    if r22.status_code == 200:
        obj = r22.json()
        print (obj)
 check()
def check_in():
    global myid
    myid= input('Select the ID #\n')
    print("User ID %s " %(myid))
    https = "https://"
    url2 = "api/config/v1/vault/account/"
    url3 = "/force-check-in"
    url = https + url1 + url2 + myid + url3
    payload = "{ \"id\": \"%s\"}" '' %(myid)
    headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer %s' %format,
}

    r33 = requests.request("POST", url, headers=headers, data = payload)
    if r33.status_code == 200:
        print ("CheckIn Completed")
    else:
        print (r33.text.encode('utf8'))
check_in()
