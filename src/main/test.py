import requests;

auth_data = {'email': 'cezar_31@hotmail.com', 'pass': 'DF0$tu0'}
resp = requests.post('https://www.facebook.com/', data=auth_data)

print(resp)
