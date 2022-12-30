import requests

if __name__ == '__main__':
    url = "https://www.baidu.com"
    x = requests.get(url)
    x.encoding = "utf-8"
    print(x.text)
