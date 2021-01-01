import urllib.request, urllib.parse, urllib.error
import json
import ssl

# code for ignoring SSL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0

user_url = input('Enter URL:')
if len(user_url) <1 :
    print("enter correct URL")

uh = urllib.request.urlopen(user_url, context = ctx).read().decode()
#data = uh.decode()
#print(uh)

js = json.loads(uh)

#print('============================')

count_list = js['comments']
length = len(count_list)
print("number of names: ",length)

for item in count_list:
    count = item['count']
    total = total +count
    print("count is:", count, " Total is:", total)
