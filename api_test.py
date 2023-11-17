from pprint import pprint

from requests import get, post
params = {
    "name": "First",
    "code": 56
}
# 28 code
# for i in range(60):
d = get("http://127.0.0.1:5000/create_server", params=params).json()

print(d)

a = get("http://127.0.0.1:5000/get_server", params=params).json()
print(a)