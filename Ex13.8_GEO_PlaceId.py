import urllib.request, urllib.parse, urllib.error
import ssl
import json

# for ssl errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

di = dict()

serviceurl = "http://py4e-data.dr-chuck.net/json?"

# just like twitter oAuth, Dr Chuck's geo website has an auth key = 42
# you need to use this to access the geocode

di['key']=42

inputadd = input("Enter Address:")
di['address']= inputadd
url =  serviceurl+urllib.parse.urlencode(di)
print("Retreiving data from:", url)


###### now we have the final URL to be used
##### this url now needs to be opened, decoded and then loaded
##### to be read out as final strings

jsd = urllib.request.urlopen(url, context = ctx).read().decode()

# in the above code context is used for SSL
# the above line will give a dictionary as an output
# this dictionary then needs to be converted into a list using json.loads()

info = json.loads(jsd)

# to check indentation, use dumps() to check the key:value type=
info_indented = json.dumps(info, indent =4)
print('=======this is the output indented; to check the key:value type============')
print(info_indented)

final = info['results'][0]['place_id']
print(final)
