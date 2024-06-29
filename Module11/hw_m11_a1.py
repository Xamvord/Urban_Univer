import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    data = response.json()
    for post in data[:5]:
        print(f"ID: {post['id']}, Title: {post['title']}")
else:
    print(f"Ошибка: {response.status_code}")

print()
print('# ------------------------------------------------------------------------------------- #')

payload = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)

if response.status_code == 201:
    data = response.json()
    print(f"Создан пост с ID: {data['id']}")
else:
    print(f"Ошибка: {response.status_code}")

print()
print('# ------------------------------------------------------------------------------------- #')

url = 'https://jsonplaceholder.typicode.com/posts/invalid'

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"OOps: Something Else: {err}")
