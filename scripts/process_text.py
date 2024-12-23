import requests

def main():
    url = "http://127.0.0.1:8000/process_text"
    text = "С другой стороны, базовый вектор развития играет определяющее значение для переосмысления внешнеэкономических политик. В своём стремлении улучшить пользовательский опыт мы упускаем, что активно развивающиеся страны третьего мира лишь добавляют фракционных разногласий и подвергнуты целой серии независимых исследований. Для современного мира современная методология разработки предоставляет широкие возможности для направлений прогрессивного развития."
    response = requests.post(url, json={"text": text})
    processed_text = response.json()
    print(processed_text['tokens'])


if __name__ == '__main__':
    main()