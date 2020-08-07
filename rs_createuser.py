
def create_user():
    """ Create user"""
    global url1
    https = "https://"
    url2 = ".beyondtrustcloud.com/api/config/v1/user"
    url = https + url1 + url2
    username=input('username\n')
    id=input('ID#\n')
    public_display_name=input('public_Display_Name\n')
    security_provider_id=input('securityID#\n')
    payload = "{\"username\":\"%s\",\"id\":\"%s\",\"public_display_name\":\"%s\",\"security_provider_id\":\"%s\"}" '' %(username,id,public_display_name,security_provider_id)
    headers = {
   'authorization' : 'Bearer %s' %format,
    'Content-Type': 'application/json'
}
    ri = requests.request("POST", url, headers=headers, data = payload)
    print(ri.text.encode('utf8'))
create_user()
