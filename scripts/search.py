import requests

def main():
    url = "http://127.0.0.1:8000/search"
    text = "Наушники с хорошим звуком"
    response = requests.post(url, json={"text": text})
    res = response.json()
    print(res['results'])


if __name__ == '__main__':
    main()