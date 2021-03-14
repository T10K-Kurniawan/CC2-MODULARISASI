import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    print(f'succes! {response}') print(f"content {response.text}")
except Exception as e:
    print(f'smthing wrong {e})
print('program ended')


