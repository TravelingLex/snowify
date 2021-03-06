import requests
import json
import urllib.request as request
import config

# with request.urlopen('https://api.weatherunlocked.com/api/snowreport/13003?app_id=fd2cdee9&app_key=cbe14ed2a206c188303087c3bfd80202') as response:
#     if response.getcode() == 200:
#         source = response.read()
#         data = json.loads(source)
#     else:
#         print('An error occurred while attempting to retrieve the API data.')
    
# type(data)
# data.keys()
# type(data['lowersnow_in'])
# print(type(data['lowersnow_in']).float)
api_id = config.api_id
api_key = config.api_key



forecast_request = requests.get(config.forecast_url)
forecast_report = forecast_request.json()
print(forecast_report)
print("Lower snow report:",forecast_report['lowersnow_in'],"inches.")
if forecast_report['newsnow_in'] >= 3:
    print('You got Snow!')
    print('The last snowfall size was',forecast_report['lastsnow_in'],'inches.')
    print('The snow type is',forecast_report['conditions'],'.')
else:
    print('Hopefully soon!')
    print('The last snowfall size was',forecast_report['lastsnow_in'],'inches on',forecast_report['lastsnow'])

