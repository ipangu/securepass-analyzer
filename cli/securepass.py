import requests

def analyze_password(password):
    response = requests.post(
        "http://localhost:5000/api/analyze",
        json={"password": password}
    )
    return response.json()

if __name__ == "__main__":
    password = input("Enter password to analyze: ")
    result = analyze_password(password)
    print(f"Strength: {result['strength']}\nMessage: {result['message']}")

