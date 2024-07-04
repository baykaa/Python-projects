import requests
length = '16'
api_url = 'https://api.api-ninjas.com/v1/passwordgenerator?length={}'.format(length)
response = requests.get(api_url, headers={'X-Api-Key': 'jFkXpJH4+SxxKnwov9mD5Q==tTehIShdbVrjJXYw'})
if response.status_code == requests.codes.ok:
    print(response.text)
    print(response["random_password"])
else:
    print("Error:", response.status_code, response.text)
