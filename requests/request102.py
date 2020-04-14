import requests


def main():
    payload = {"base": "USD", "symbols": "SEK"}
    response = requests.get("https://api.exchangeratesapi.io/latest", params=payload)
    if response.status_code != 200:
        print(f'Status Code:', response.status_code)
        raise Exception('There was an Error')

    data = response.json()
    print(f'Json data: {data}')


if __name__ == "__main__":
    main()
