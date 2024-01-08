from urllib import request

target = request.urlopen("https://google.com")
print(target.read())