import urllib
import requests
main_api='http://maps.googleapis.com/maps/api/geocode/json?'
address='lhr'
url=main_api+urllib.parse.urlencode({'address':address})
print (url)

json_data=requests.get(url).json()

json_status=json_data['status']
print('API Status : ' + json_status)

print (json_data)
formatted_address=json_data['results'][0]['formatted_address']
print (formatted_address)
