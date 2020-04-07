# urllib 库的使用

# import urllib request
from urllib import request

url = "http://www.baidu.com"
response = request.urlopen(url, timeout=1)
result = response.read().decode("utf-8")
print(result)
