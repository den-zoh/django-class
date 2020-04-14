import requests

def main():
    response = requests.get("https://www.google.com/machassoe")
    print(f'Status Code: {response.status_code}')
    print('Header:', response.headers['Content-Type'])
    print(f'Encoding type: {response.encoding}')



if __name__ == "__main__":
    main()
