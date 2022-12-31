import requests

if __name__ == '__main__':
    url = "https://fanyi.baidu.com/langdetect"
    param = {"query": "dog"}
    x = requests.post(url, param)
    x.encoding = "utf-8"
    print(x.text)
