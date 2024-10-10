import requests


serviceKey = ''
url = ''
params={'serviceKey':serviceKey, 'YM':'201201', 'NAT_CD':'112','ED_CD':'E'}

response = requests.get(url, params=params)
print(response.content)
print()
print('import requests testing')
